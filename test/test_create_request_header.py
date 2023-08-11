from zalo_sdk.BaseClient import BaseClient
from zalo_sdk.oa.ZaloMessage import *

from . import ZaloSendMessage


class ZaloSendRequestHeader(ZaloSendMessage):

    def test_create_request_header(self):
        client = BaseClient(
            app_id=self.app_id, 
            secret_key=self.secret_key, 
            access_token=self.access_token, 
            refresh_token=self.refresh_token
        )

        header = client.create_request_header(method="POST")

        data = {
            'Content-Type': "application/json",
            'access_token': self.access_token,
        }

        self.assertEqual(header, data)

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

    def test_send_file_header(self):
        client = BaseClient(
            app_id=self.app_id, 
            secret_key=self.secret_key, 
            access_token=self.access_token, 
            refresh_token=self.refresh_token
        )

        
        # Call the create_request_header function and assert the response
        header = client.create_request_header(method="GET", type="file")

        data = {
            'access_token': self.access_token,
        }

        self.assertEqual(header, data)
