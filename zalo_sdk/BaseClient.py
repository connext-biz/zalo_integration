import datetime
import requests
import json
import zalo_sdk

import urllib.parse


class BaseClient:
    def __init__(self, access_token="", refresh_token="", app_id="", secret_key=""):
        self._refresh_token = refresh_token
        self._access_token = access_token
        self._app_id = app_id
        self._secret_key = secret_key
        self._expire_at = 0

    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, token):
        self._refresh_token = token

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, token):
        self._access_token = token

    def send_request(self, method: str, url: str, body: dict = None, params: dict = None, xtra_headers: str = {}):
        """
        Send a request to Zalo, adding required tokens

        Params:
        :method: Either POST or GET
        :url: The Zalo endpoints to send the request
        :params: GET params to send with GET method
        :body: The body of POST request. If it is set in GET request, the body
               will be converted to JSON string and set the data param.
        :xtra_headers: Other HTTP headers to set with this request
        """
        if method == "POST":
            headers = {
                'Content-Type': "application/json",
                'access_token': self._access_token,
                **xtra_headers
            }
            if body is None:
                body = {}
            response = requests.post(
                url,
                json=body,
                headers=headers)
        elif method == "GET":
            headers = {
                'access_token': self._access_token
            }
            if params is None:
                params = {}
            if body is not None:
                # Encode body to json string and set data param
                params["data"] = json.dumps(body)
            response = requests.get(
                url,
                params=params,
                headers=headers)
        else:
            raise Exception(f"Unknown method '{method}'")
        return response

    def check_http_error(self, response: requests.Response):
        if response.status_code != 200:
            raise Exception(
                f"HTTP Error {response.status_code}: {response.text}")

    def check_zalo_zns_error(self, response):
        if "error" in response and response["error"] != 0:
            if "message" in response:
                if response["error"] == -124:
                    raise zalo_sdk.ZaloOAAuthTokenExpiredException(
                        response["error"], response["message"])
                raise zalo_sdk.ZaloException(
                    response["error"], response["message"])
            raise zalo_sdk.ZaloException(response["error"])

    def check_zalo_oa_error(self, response):
        if "error" in response and response["error"] != 0:
            if "message" in response:
                if response["error"] == -216 and "expired" in response["message"]:
                    raise zalo_sdk.ZaloOAAuthTokenExpiredException(
                        response["error"], response["message"])
                raise zalo_sdk.ZaloOAException(
                    response["error"], response["message"])
            raise zalo_sdk.ZaloOAException(response["error"])

    def request_authoriation_code_url(self, callback_url, code_challenge=None, state=None):
        """
        Get the URL to request the authorization code.

        Official Documentation:
        https://developers.zalo.me/docs/api/official-account-api/xac-thuc-va-uy-quyen/cach-1-xac-thuc-voi-giao-thuc-oauth/yeu-cau-cap-moi-oa-access-token-post-4307
        """
        base_url = "https://oauth.zaloapp.com/v4/oa/permission"
        parsed_url = urllib.parse.urlparse(base_url)
        params = {
            'app_id': self._app_id,
            'redirect_uri': callback_url,
        }
        if code_challenge is not None:
            params['code_challenge'] = code_challenge
        if state is not None:
            params['state'] = state

        auth_url = parsed_url._replace(query=urllib.parse.urlencode(params))
        return auth_url.geturl()

    def isAccessTokenExpired(self):
        return self._expire_at != 0 and self._expire_at < datetime.datetime.utcnow().timestamp()
        # If expire_at == 0, skip the check

    def check_and_set_token(self, zalo_response):
        if 'refresh_token' not in zalo_response:
            raise zalo_sdk.ZaloException(-1,
                                         "'refresh_token' not found in the response")
        if 'access_token' not in zalo_response:
            raise zalo_sdk.ZaloException(-1,
                                         "'access_token' not found in the response")

        expire_in = int(zalo_response.get("expires_in", 0))
        expire_at = datetime.datetime.now()+datetime.timedelta(seconds=expire_in)
        self._refresh_token = zalo_response['refresh_token']
        self._access_token = zalo_response['access_token']
        self._expire_at = int(expire_at.timestamp())

    def get_access_token_from_authorization_code(self, authorization_code: str, code_verifier: str):
        zalo_get_access_token_url = "https://oauth.zaloapp.com/v4/oa/access_token"
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'secret_key': self._secret_key
        }
        body = {
            'code': authorization_code,
            'app_id': self._app_id,
            'grant_type': 'authorization_code',
            'code_verifier': code_verifier
        }

        response = requests.post(
            zalo_get_access_token_url, data=body, headers=headers)
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_oa_error(zalo_response)
        self.check_and_set_token(zalo_response)

        return self._access_token, self._refresh_token, self._expire_at

    def refresh_acccess_token(self):
        zalo_get_access_token_url = "https://oauth.zaloapp.com/v4/oa/access_token"
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'secret_key': self._secret_key
        }
        body = {
            'refresh_token': self._refresh_token,
            'app_id': self._app_id,
            'grant_type': 'refresh_token'
        }

        response = requests.post(
            zalo_get_access_token_url, data=body, headers=headers)
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_oa_error(zalo_response)
        self.check_and_set_token(zalo_response)

        return self._access_token, self._refresh_token, self._expire_at
