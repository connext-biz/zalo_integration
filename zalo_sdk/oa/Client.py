# Copyright (c) 2023, TNT International Trading Corp.
# All rights reserved.

import requests
import urllib.parse
from zalo_sdk import BaseClient


class Client(BaseClient):
    def __init__(self, app_id, secret_key):
        super(BaseClient)
        self.app_id = app_id
        self.secret_key = secret_key

    def get_authoriation_code(self, callback_url):
        escaped_url = urllib.parse.quote(callback_url, safe='')
        auth_url = f"https://oauth.zaloapp.com/v4/oa/permission?app_id={self.app_id}&redirect_uri={escaped_url}"

        return auth_url

    def get_access_token(self, authorization_code) -> tuple[str, str]:
        zalo_get_access_token_url = "https://oauth.zaloapp.com/v4/oa/access_token"
        headers = {}
        headers['Content-Type'] = "application/x-www-form-urlencoded"
        headers['secret_key'] = self.secret_key
        body = {
            'code': authorization_code,
            'app_id': self.app_id,
            'grant_type': 'authorization_code',
            'code_verifier': 'your_code_verifier'
        }

        response = requests.post(
            zalo_get_access_token_url, data=body, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")

        zalo_response = response.json()
        if 'refresh_token' not in zalo_response:
            raise Exception("Error: 'refresh_token' not found in the response")
        if 'access_token' not in zalo_response:
            raise Exception("Error: 'access_token' not found in the response")

        self.refresh_token = zalo_response['refresh_token']
        self.access_token = zalo_response['access_token']

        return self.access_token, self.refresh_token

    def refresh_acccess_token(self) -> tuple[str, str]:
        zalo_get_access_token_url = "https://oauth.zaloapp.com/v4/oa/access_token"
        headers = {}
        headers['Content-Type'] = "application/x-www-form-urlencoded"
        headers['secret_key'] = self.secret_key
        body = {
            'refresh_token': self._refresh_token,
            'app_id': self.app_id,
            'grant_type': 'refresh_token'
        }

        response = requests.post(
            zalo_get_access_token_url, data=body, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")

        zalo_response = response.json()
        if 'refresh_token' not in zalo_response:
            raise Exception("Error: 'refresh_token' not found in the response")
        if 'access_token' not in zalo_response:
            raise Exception("Error: 'access_token' not found in the response")

        self.refresh_token = zalo_response['refresh_token']
        self.access_token = zalo_response['access_token']

        return self.access_token, self.refresh_token

    def send_message_to_user(self, user_id: str, message: str):
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
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")
        zalo_response = response.json()
        return zalo_response

    def send_response_to_user(self, message_id: str, message: str):
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
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")
        zalo_response = response.json()
        return zalo_response

    def get_free_response_quota(self, message_id: str):
        body = {
            "message_id": message_id
        }
        response = self.send_request(
            "POST", "https://openapi.zalo.me/v2.0/oa/quota/message", body)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")
        zalo_response = response.json()
        return zalo_response

    def get_profile(self, user_id: str):
        params = {
            "user_id": user_id
        }
        response = self.send_request(
            "GET", "https://openapi.zalo.me/v2.0/oa/getprofile", params
        )
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")
        zalo_response = response.json()
        return zalo_response