import unittest

import requests


class ZaloSendMessage(unittest.TestCase):
    def setUp(self):
        # Set up the test data and objects if needed
        self.user_id = ""
        self.access_token = ""

    def test_send_text_message(self):
        """
        read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-tu-van/gui-tin-tu-van-dang-van-ban
        """
        url = "https://openapi.zalo.me/v3.0/oa/message/cs"

        headers = {
            "access_token": self.access_token,
            "Content-Type": "application/json",
        }

        data = {
            "recipient": {"user_id": self.user_id},
            "message": {"text": "hello, world!"},
        }

        response = requests.post(url, json=data, headers=headers)
        print(response.json())


if __name__ == "__main__":
    unittest.main()
