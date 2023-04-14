import requests
import json


class BaseClient:
    def __init__(self, access_token="", refresh_token=""):
        self._refresh_token = refresh_token
        self._access_token = access_token

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

    def send_request(self, method, url, body):
        if method == "POST":
            headers = {
                'Content-Type': "application/json",
                'access_token': self._access_token
            }
            response = requests.post(
                url,
                json=body,
                headers=headers)
        elif method == "GET":
            headers = {
                'access_token': self._access_token
            }
            response = requests.get(
                url,
                params={"data": json.dumps(body)},
                headers=headers)
        else:
            raise Exception(f"Unknown method '{method}'")
        return response

    def check_http_error(self, response: requests.Response):
        if response.status_code != 200:
            raise Exception(
                f"HTTP Error {response.status_code}: {response.text}")
