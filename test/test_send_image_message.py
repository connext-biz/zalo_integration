import unittest

import requests


class ZaloSendMessage(unittest.TestCase):
    def setUp(self):
        # Set up the test data and objects if needed
        self.user_id = ""
        self.access_token = ""

    def test_send_image_message(self):
        """
        read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-tu-van/gui-tin-tu-van-dinh-kem-anh
        """
        url = "https://openapi.zalo.me/v3.0/oa/message/cs"

        headers = {
            "access_token": self.access_token,
            "Content-Type": "application/json",
        }

        data = {
            "recipient": {"user_id": self.user_id},
            "message": {
                "text": "Zalo đạt 100 triệu người dùng",
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "media",
                        "elements": [
                            {
                                "media_type": "image",
                                "url": "https://stc-developers.zdn.vn/images/bg_1.jpg",
                            }
                        ],
                    },
                },
            },
        }

        response = requests.post(url, json=data, headers=headers)
        print(response.json())


if __name__ == "__main__":
    unittest.main()
