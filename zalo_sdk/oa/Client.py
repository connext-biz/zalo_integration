# Copyright (c) 2023, TNT International Trading Corp.
# All rights reserved.

import datetime
import requests
import urllib.parse
from zalo_sdk import BaseClient
from zalo_sdk.oa import ZaloOAException


class Client(BaseClient):
    def __init__(self, app_id, secret_key):
        super(BaseClient)
        self.app_id = app_id
        self.secret_key = secret_key
        self.expire_at = 0

    def isAccessTokenExpired(self):
        return self.expire_at != 0 and self.expire_at < datetime.datetime.utcnow().timestamp()
        # If expire_at == 0, skip the check

    def check_zalo_error(self, response):
        if "error" in response and response["error"] != 0:
            if "message" in response:
                raise ZaloOAException(response["error"], response["message"])
            else:
                raise ZaloOAException(response["error"])

    def request_authoriation_code_url(self, callback_url, challenge_string=None):
        """
        Get the URL to request the authorization code.

        Official Documentation: https://developers.zalo.me/docs/api/official-account-api/xac-thuc-va-uy-quyen/cach-1-xac-thuc-voi-giao-thuc-oauth/lay-oa-access-token-tu-oa-refresh-token-post-4970
        """
        base_url = "https://oauth.zaloapp.com/v4/oa/permission"
        parsed_url = urllib.parse.urlparse(base_url)
        params = {
            'app_id': self.app_id,
            'redirect_uri': callback_url,
        }
        if challenge_string is not None:
            params['state'] = challenge_string

        auth_url = parsed_url._replace(query=urllib.parse.urlencode(params))
        return auth_url.geturl()

    def check_and_set_token(self, zalo_response):
        if 'refresh_token' not in zalo_response:
            raise ZaloException(-1,
                                "'refresh_token' not found in the response")
        if 'access_token' not in zalo_response:
            raise ZaloException(-1, "'access_token' not found in the response")

        expire_in = int(zalo_response.get("expires_in", 0))
        expire_at = datetime.datetime.now()+datetime.timedelta(seconds=expire_in)
        self.refresh_token = zalo_response['refresh_token']
        self.access_token = zalo_response['access_token']
        self.expire_at = int(expire_at.timestamp())

    def get_access_token_from_authorization_code(self, authorization_code):
        zalo_get_access_token_url = "https://oauth.zaloapp.com/v4/oa/access_token"
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'secret_key': self.secret_key
        }
        body = {
            'code': authorization_code,
            'app_id': self.app_id,
            'grant_type': 'authorization_code',
            'code_verifier': 'your_code_verifier'
        }

        response = requests.post(
            zalo_get_access_token_url, data=body, headers=headers)
        self.check_http_response(response)

        zalo_response = response.json()
        self.check_zalo_error(zalo_response)
        self.check_and_set_token(zalo_response)

        return self.access_token, self.refresh_token, self.expire_at

    def refresh_acccess_token(self):
        zalo_get_access_token_url = "https://oauth.zaloapp.com/v4/oa/access_token"
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'secret_key': self.secret_key
        }
        body = {
            'refresh_token': self._refresh_token,
            'app_id': self.app_id,
            'grant_type': 'refresh_token'
        }

        response = requests.post(
            zalo_get_access_token_url, data=body, headers=headers)
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_error(zalo_response)
        self.check_and_set_token(zalo_response)

        return self.access_token, self.refresh_token, self.expire_at

    def send_message_to_user(self, user_id, message):
        body = {
            "recipient": {
                "user_id": user_id
            },
            "message": {
                "text": message
            }
        }
        response = self.send_request(
            "POST", "https://openapi.zalo.me/v2.0/oa/message", body)
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_error(zalo_response)

        return zalo_response

    def send_response_to_user(self, message_id, message):
        body = {
            "recipient": {
                "message_id": message_id
            },
            "message": {
                "text": message
            }
        }
        response = self.send_request(
            "POST", "https://openapi.zalo.me/v2.0/oa/message", body)
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_error(zalo_response)

        return zalo_response

    def get_free_response_quota(self, message_id):
        body = {
            "message_id": message_id
        }
        response = self.send_request(
            "POST", "https://openapi.zalo.me/v2.0/oa/quota/message", body)
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_error(zalo_response)

        return zalo_response

    def get_profile(self, user_id):
        params = {
            "user_id": user_id
        }
        response = self.send_request(
            "GET", "https://openapi.zalo.me/v2.0/oa/getprofile", params
        )
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_error(zalo_response)

        return zalo_response