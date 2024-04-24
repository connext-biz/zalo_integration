from zalo_sdk.oa.Client import Client
from zalo_sdk.oa.ZaloMessage import *

from . import ZaloSendMessage


class ZaloGetUserDetail(ZaloSendMessage):

    def test_get_user_detail(self):
        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the get_user_detail function and assert the response
        generated_result = client.get_user_detail(user_id=self.user_id)

        expected_result = {
        }

        self.assertEqual(generated_result, expected_result)
