import zalo_sdk
from enum import Enum


class ZNSTemplateStatus(Enum):
    Enabled = 1
    PendingReview = 2
    Reject = 3
    Disabled = 4


class Client(zalo_sdk.BaseClient):
    def __init__(self, app_id, secret_key, access_token="", refresh_token=""):
        super(Client, self).__init__(app_id=app_id, secret_key=secret_key,
                                     access_token=access_token, refresh_token=refresh_token)

    def get_template_list(self, offset: int, limit: int, status: ZNSTemplateStatus = None):
        params = {
            "offset": offset,
            "limit": limit,
        }
        if status is not None:
            params["status"] = status.value
        response = self.send_request(
            "GET", "https://business.openapi.zalo.me/template/all", params=params
        )
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_zns_error(zalo_response)

        return zalo_response

    def send_zns_message(self, contact_phone: str, template_id: str, template_data: dict, tracking_id: str = None, dev_mode: bool = False):
        body = {
            "phone": contact_phone,
            "template_id": template_id,
            "template_data": template_data,
        }
        if tracking_id is not None:
            body["tracking_id"] = tracking_id
        if dev_mode==True:
            body["mode"] = "development"

        response = self.send_request(
            "POST", "https://business.openapi.zalo.me/message/template", body=body)
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_zns_error(zalo_response)

        return zalo_response
