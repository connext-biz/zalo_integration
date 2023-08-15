# Copyright (c) 2023, TNT International Trading Corp.
# All rights reserved.

import zalo_sdk
import io


class Client(zalo_sdk.BaseClient):
    def __init__(self, app_id, secret_key, access_token="", refresh_token=""):
        super(Client, self).__init__(app_id=app_id, secret_key=secret_key,
                                     access_token=access_token, refresh_token=refresh_token)
        
    def create_request_body(self, recipient, body=None, action=None):
        msg_obj = zalo_sdk.oa.ZaloMessage(
            recipient=recipient,
            message_body=body,
            action=action
        )
        return msg_obj.toDict()

    def send_message(self, recipient, body=None, action=None, category="consultant", files=None):
        if category == "consultant":
            url = "https://openapi.zalo.me/v3.0/oa/message/cs"
        elif category == "transaction":
            url = "https://openapi.zalo.me/v3.0/oa/message/transaction"
        elif category == "media":
            url = "https://openapi.zalo.me/v3.0/oa/message/promotion"
        else:
            raise ValueError("Invalid message category provided.")
        
        msg_header = self.create_request_header(method="POST")
        msg_body = self.create_request_body(recipient, body, action)
        
        response = self.send_request(
            method="POST", url=url, body=msg_body, headers=msg_header, files=files)
        return self._validate_zalo_response(response)
    
    def upload_file(self, file_data: bytes, file_type: str = "file", file_name: str = "", mime_type: str = ""):
        headers = self.create_request_header(method="POST", type="file")
        if file_type == "file":
            url = "https://openapi.zalo.me/v2.0/oa/upload/file"
        elif file_type == "image":
            url = "https://openapi.zalo.me/v2.0/oa/upload/image"
        else:
            raise ValueError("Invalid file type provided.")
        files = {
            "file": (file_name, io.BytesIO(file_data), mime_type)
        }
        response = self.send_request(
            method="POST", url=url, headers=headers, files=files)
        return self._validate_zalo_response(response)

    def get_free_response_quota(self, message_id):
        headers = self.create_request_header(method="POST")
        body = {
            "message_id": message_id
        }
        response = self.send_request(
            method="POST", url="https://openapi.zalo.me/v2.0/oa/quota/message", body=body, headers=headers)
        return self._validate_zalo_response(response)

    def get_profile(self, user_id):
        headers = self.create_request_header(method="GET")
        params = {
            "user_id": user_id
        }
        response = self.send_request(
            method="GET", url="https://openapi.zalo.me/v2.0/oa/getprofile", body=params, headers=headers
        )
        return self._validate_zalo_response(response)
    
    def _validate_zalo_response(self, response):
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_oa_error(zalo_response)
        return zalo_response        



