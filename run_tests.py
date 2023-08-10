import unittest
from test.test_oa_create_request_body import ZaloSendRequestBody
from test.test_create_request_header import ZaloSendRequestHeader

def create_test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloSendRequestBody))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloSendRequestHeader))

    return test_suite

if __name__ == "__main__":
    suite = create_test_suite()

    runner = unittest.TextTestRunner(verbosity=2)

    result = runner.run(suite)

    print()
