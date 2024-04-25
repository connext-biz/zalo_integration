from zalo_sdk.oa.Client import Client
from zalo_sdk.oa.ZaloMessage import *

from . import ZaloSendMessage


class ZaloGetZaloQuotas(ZaloSendMessage):

    def test_get_zalo_oa_quotas(self):
        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the get_zalo_oa_quotas function and assert the response
        generated_result = client.get_zalo_oa_quotas(quota_owner="OA")

        expected_result = {
            'data': [
                {
                    'asset_id': '8c273149281ac144980b', 
                    'product_type': 'cs', 
                    'quota_type': 'sub_quota', 
                    'valid_through': '30/04/2024', 
                    'total': 2000, 
                    'remain': 1997
                }
            ], 
            'error': 0, 
            'message': 'Success'
        }
        self.assertEqual(generated_result, expected_result)

    def test_get_zalo_oa_quotas_with_all_params(self):
        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the get_zalo_oa_quotas function and assert the response
        generated_result = client.get_zalo_oa_quotas(quota_owner="OA", quota_type="sub_quota", product_type="cs")

        expected_result = {
            'data': [
                {
                    'asset_id': '8c273149281ac144980b', 
                    'product_type': 'cs', 
                    'quota_type': 'sub_quota', 
                    'valid_through': '30/04/2024', 
                    'total': 2000, 
                    'remain': 1997
                }
            ], 
            'error': 0, 
            'message': 'Success'
        }
        self.assertEqual(generated_result, expected_result)

    def test_get_zalo_oa_quotas_with_valid_product_type(self):
        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)
        # Call the get_zalo_oa_quotas function and assert the response
        generated_result = client.get_zalo_oa_quotas(quota_owner="OA", product_type="cs")

        expected_result = {
            'data': [
                {
                    'asset_id': '8c273149281ac144980b', 
                    'product_type': 'cs', 
                    'quota_type': 'sub_quota', 
                    'valid_through': '30/04/2024', 
                    'total': 2000, 
                    'remain': 1997
                }
            ], 
            'error': 0, 
            'message': 'Success'
        }
        self.assertEqual(generated_result, expected_result)

    def test_get_zalo_oa_quotas_with_wrong_product_type(self):
        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        with self.assertRaises(ValueError) as e:
            # Call the get_zalo_oa_quotas function and assert the response
            client.get_zalo_oa_quotas(quota_owner="OA", product_type="csgo")
        self.assertEqual(str(e.exception), "Invalid product_type: csgo. Valid values are: cs, transaction")


    def test_get_zalo_user_quotas(self):
        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the get_zalo_user_quotas function and assert the response
        generated_result = client.get_zalo_user_quotas(user_id=self.user_id)

        expected_result = {
            'data': {
                'last_interaction': '1712765640000', 
                'cs_reply': {
                    'remain': 0, 
                    'total': 0
                }, 
                'promotion': {
                    'daily_remain': 1, 
                    'daily_total': 1, 
                    'monthly_remain': 4, 
                    'monthly_total': 4
                }
            }, 
            'error': 0, 
            'message': 'Success'
        }
        self.assertEqual(generated_result, expected_result)
