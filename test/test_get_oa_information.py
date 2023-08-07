from zalo_sdk.oa.Client import Client
from zalo_sdk.oa.ZaloMessage import *
from zalo_sdk.BaseClient import BaseClient

from . import ZaloSendMessage


class ZaloGetOAInfoMessage(ZaloSendMessage):
    """
        read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-tu-van/gui-tin-tu-van-dang-van-ban
    """

    def test_get_oa_information(self):
        client = BaseClient(
            app_id=self.app_id, 
            secret_key=self.secret_key, 
            access_token=self.access_token, 
            refresh_token=self.refresh_token
        )

        # Call the create_request_header function and assert the response
        response = client.send_request(
            method="GET",
            url="https://openapi.zalo.me/v2.0/oa/getoa",
        )
        result = response.json()

        self.assertEqual(result["error"], 0)

    
    def test_get_oa_information_with_wrong_method(self):
        client = BaseClient(
            app_id=self.app_id, 
            secret_key=self.secret_key, 
            access_token=self.access_token, 
            refresh_token=self.refresh_token
        )

        # Call the create_request_header function and assert the response
        response = client.send_request(
            method="POST",
            url="https://openapi.zalo.me/v2.0/oa/getoa",
        )
        result = response.json()

        self.assertEqual(result["error"], -200)

    def test_get_oa_information_header(self):
        client = BaseClient(
            app_id=self.app_id, 
            secret_key=self.secret_key, 
            access_token=self.access_token, 
            refresh_token=self.refresh_token
        )

        
        # Call the create_request_header function and assert the response
        header = client.create_request_header(method="GET")

        data = {
            'access_token': self.access_token,
        }

        self.assertEqual(header, data)
