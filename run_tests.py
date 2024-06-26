import unittest
from test.test_oa_create_request_body import ZaloSendRequestBody
from test.test_create_request_header import ZaloSendRequestHeader
from test.test_get_user_detail import ZaloGetUserDetail
from test.test_get_zalo_quotas import ZaloGetZaloQuotas

def create_test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloSendRequestBody))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloSendRequestHeader))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloGetUserDetail))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloGetZaloQuotas))

    return test_suite

if __name__ == "__main__":
    suite = create_test_suite()

    runner = unittest.TextTestRunner(verbosity=2)

    result = runner.run(suite)

    print()
