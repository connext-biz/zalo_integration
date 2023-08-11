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

        generated_header = client.create_request_header(method="POST")

        expected_header = {
            'Content-Type': "application/json",
            'access_token': self.access_token,
        }

        self.assertEqual(generated_header, expected_header)

    def test_get_oa_information_header(self):
        client = BaseClient(
            app_id=self.app_id, 
            secret_key=self.secret_key, 
            access_token=self.access_token, 
            refresh_token=self.refresh_token
        )

        
        # Call the create_request_header function and assert the response
        generated_header = client.create_request_header(method="GET")

        expected_header = {
            'access_token': self.access_token,
        }

        self.assertEqual(generated_header, expected_header)

    def test_send_file_header(self):
        client = BaseClient(
            app_id=self.app_id, 
            secret_key=self.secret_key, 
            access_token=self.access_token, 
            refresh_token=self.refresh_token
        )

        
        # Call the create_request_header function and assert the response
        generated_header = client.create_request_header(method="GET", type="file")

        expected_header = {
            'access_token': self.access_token,
        }

        self.assertEqual(generated_header, expected_header)
