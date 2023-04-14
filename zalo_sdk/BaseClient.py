import requests
import json

class BaseClient:
    def __init__(self, access_token: str = "", refresh_token: str = ""):
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

    def send_request(self, method: str, url: str, body: object | str) -> requests.Response:
        match method:
            case "POST":
                headers = {
                    'Content-Type': "application/json",
                    'access_token': self._access_token
                }
                response = requests.post(
                    url,
                    json=body,
                    headers=headers)
            case "GET":
                headers = {
                    'access_token': self._access_token
                }
                response = requests.get(
                    url,
                    params={"data": json.dumps(body)},
                    headers=headers)
            case _:
                raise Exception(f"Unknown method '{method}'")
        return response
