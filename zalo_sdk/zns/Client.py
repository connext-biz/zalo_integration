import zalo_sdk
from enum import Enum


class ZNSTemplateStatus(Enum):
    Enabled = 1
    PendingReview = 2
    Reject = 3
    Disabled = 4


class Client(zalo_sdk.BaseClient):
    def __init__(self, app_id, secret_key, access_token="", refresh_token="", **kwargs):
        super(Client, self).__init__(app_id=app_id, secret_key=secret_key,
                                     access_token=access_token, refresh_token=refresh_token,
                                     **kwargs)
        self.endpoint_prefix = kwargs['endpoint_prefix'] if 'endpoint_prefix' in kwargs else "https://business.openapi.zalo.me"

    def get_template_list(self, offset: int, limit: int, status: ZNSTemplateStatus = None):
        params = {
            "offset": offset,
            "limit": limit,
        }
        if status is not None:
            params["status"] = status.value

        msg_header = self.create_request_header(method="GET")
        url = f"{self.endpoint_prefix}/template/all"
        response = self.send_request(
            method="GET", url=url, params=params, headers=msg_header
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

        msg_header = self.create_request_header(method="POST")

        url = f"{self.endpoint_prefix}/message/template"
        response = self.send_request(
            method="POST", url=url, body=body, headers=msg_header)
        self.check_http_error(response)

        zalo_response = response.json()
        self.check_zalo_zns_error(zalo_response)

        return zalo_response
