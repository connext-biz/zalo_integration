import unittest
from test.test_send_text_message import ZaloSendTextMessage
from test.test_send_reply_message import ZaloSendReplyMessage
from test.test_send_media_message import ZaloSendMediaMessage
from test.test_send_request_form_message import ZaloSendRequestFormMessage
from test.test_send_sticker_message import ZaloSendStickerMessage
from test.test_send_transaction_message import ZaloSendTransactionMessage
from test.test_send_file_message import ZaloSendFileMessage
from test.test_get_oa_information import ZaloGetOAInfoMessage

def create_test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloSendTextMessage))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloSendReplyMessage))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloSendMediaMessage))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloSendRequestFormMessage))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloSendStickerMessage))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloSendTransactionMessage))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloSendFileMessage))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ZaloGetOAInfoMessage))

    return test_suite

if __name__ == "__main__":
    suite = create_test_suite()

    runner = unittest.TextTestRunner(verbosity=2)

    result = runner.run(suite)

    print()
