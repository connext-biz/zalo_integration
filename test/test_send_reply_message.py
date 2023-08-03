import unittest

import requests


class ZaloSendMessage(unittest.TestCase):
    def setUp(self):
        # Set up the test data and objects if needed
        self.user_id = ""
        self.access_token = ""

    def test_send_reply_message(self):
        """
        read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-tu-van/gui-tin-tu-van-trich-dan
        """
        url = "https://openapi.zalo.me/v3.0/oa/message/cs"

        headers = {
            "access_token": self.access_token,
            "Content-Type": "application/json",
        }

        data = {
            "recipient": {"user_id": self.user_id},
            "message": {
                "text": "Chào bạn, Shop có địa chỉ là 182 Lê Đại Hành, P15, Q10, HCM",
                "quote_message_id": "75e7af1854e595bfccf0",
            },
        }

        response = requests.post(url, json=data, headers=headers)
        print(response.json())


if __name__ == "__main__":
    unittest.main()
