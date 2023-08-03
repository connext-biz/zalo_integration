import unittest

import requests


class ZaloSendMessage(unittest.TestCase):
    def setUp(self):
        # Set up the test data and objects if needed
        self.user_id = ""
        self.access_token = ""

    def test_send_request_form_message(self):
        """
        read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-tu-van/gui-tin-tu-van-theo-mau-yeu-cau-thong-tin-nguoi-dung
        """
        url = "https://openapi.zalo.me/v3.0/oa/message/cs"

        headers = {
            "access_token": self.access_token,
            "Content-Type": "application/json",
        }

        data = {
            "recipient": {"user_id": self.user_id},
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "request_user_info",
                        "elements": [
                            {
                                "title": "OA Chatbot (Testing)",
                                "subtitle": "Đang yêu cầu thông tin từ bạn",
                                "image_url": "https://developers.zalo.me/web/static/zalo.png",
                            }
                        ],
                    },
                }
            },
        }

        response = requests.post(url, json=data, headers=headers)
        print(response.json())


if __name__ == "__main__":
    unittest.main()
