# Copyright (c) 2023, TNT International Trading Corp.
# All rights reserved.

import zalo_sdk
import io


class Client(zalo_sdk.BaseClient):
    def __init__(self, app_id, secret_key, access_token="", refresh_token="", **kwargs):
        super(Client, self).__init__(app_id=app_id, secret_key=secret_key,
                                     access_token=access_token, refresh_token=refresh_token,
                                     **kwargs)
        self.endpoint_prefix = kwargs['endpoint_prefix'] if 'endpoint_prefix' in kwargs else "https://openapi.zalo.me"
        
    def create_request_body(self, recipient, body=None, action=None):
        msg_obj = zalo_sdk.oa.ZaloMessage(
            recipient=recipient,
            message_body=body,
            action=action
        )
        return msg_obj.toDict()

    def send_message(self, recipient, body=None, action=None, category="consultant", files=None):
        if category == "consultant":
            url = f"{self.endpoint_prefix}/v3.0/oa/message/cs"
        elif category == "transaction":
            url = f"{self.endpoint_prefix}/v3.0/oa/message/transaction"
        elif category == "media":
            url = f"{self.endpoint_prefix}/v3.0/oa/message/promotion"
        elif category == "action":
            url = f"{self.endpoint_prefix}/v2.0/oa/message"
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
            url = f"{self.endpoint_prefix}/v2.0/oa/upload/file"
        elif file_type == "image":
            url = f"{self.endpoint_prefix}/v2.0/oa/upload/image"
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
        url = f"{self.endpoint_prefix}/v2.0/oa/quota/message"
        response = self.send_request(
            method="POST", url=url, body=body, headers=headers)
        return self._validate_zalo_response(response)
    
    def get_zalo_oa_quotas(self, quota_owner: str, product_type: str = "", quota_type: str = ""):
        headers = self.create_request_header(method="POST")
        body = {
            "quota_owner": quota_owner,
        }
        if product_type:
            body["product_type"] = product_type
        if quota_type:
            body["quota_type"] = quota_type
        url = f"{self.endpoint_prefix}/v3.0/oa/quota/message"
        response = self.send_request(
            method="POST", url=url, body=body, headers=headers)
        return self._validate_zalo_response(response)

    def get_zalo_user_quotas(self, user_id: str):
        headers = self.create_request_header(method="POST")
        params = {
            "user_id": user_id
        }
        url = f"{self.endpoint_prefix}/v3.0/oa/quota/message"
        response = self.send_request(
            method="POST", url=url, body=params, headers=headers
        )
        return self._validate_zalo_response(response)

    def get_profile(self, user_id):
        headers = self.create_request_header(method="GET")
        params = {
            "user_id": user_id
        }
        url = f"{self.endpoint_prefix}/v2.0/oa/getprofile"
        response = self.send_request(
            method="GET", url=url, body=params, headers=headers
        )
        return self._validate_zalo_response(response)
    
    def get_user_detail(self, user_id):
        headers = self.create_request_header(method="GET")
        params = {
            "user_id": user_id
        }
        url = f"{self.endpoint_prefix}/v3.0/oa/user/detail"
        response = self.send_request(
            method="GET", url=url, body=params, headers=headers
        )
        return self._validate_zalo_response(response)
    
    def _validate_zalo_response(self, response):
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_oa_error(zalo_response)
        return zalo_response



