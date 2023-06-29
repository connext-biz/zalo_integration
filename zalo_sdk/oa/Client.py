# Copyright (c) 2023, TNT International Trading Corp.
# All rights reserved.

import zalo_sdk


class Client(zalo_sdk.BaseClient):
    def __init__(self, app_id, secret_key, access_token="", refresh_token=""):
        super(Client, self).__init__(app_id=app_id, secret_key=secret_key,
                                     access_token=access_token, refresh_token=refresh_token)

    def send_message(self, recipient, body=None, action=None):
        msg_obj = zalo_sdk.oa.ZaloMessage(
            recipient=recipient,
            message_body=body,
            action=action
        )
        response = self.send_request(
            "POST", "https://openapi.zalo.me/v3.0/oa/message/cs", msg_obj.toDict())
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_oa_error(zalo_response)
        return zalo_response

    def get_free_response_quota(self, message_id):
        body = {
            "message_id": message_id
        }
        response = self.send_request(
            "POST", "https://openapi.zalo.me/v2.0/oa/quota/message", body)
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_oa_error(zalo_response)

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
        self.check_zalo_oa_error(zalo_response)

        return zalo_response
