import unittest

import requests


class ZaloSendMessage(unittest.TestCase):
    def setUp(self):
        # Set up the test data and objects if needed
        self.user_id = ""
        self.access_token = ""

    def test_send_transaction_message(self):
        """
        read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-giao-dich/gui-tin-giao-dich
        """
        url = "https://openapi.zalo.me/v3.0/oa/message/transaction"

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
                        "template_type": "transaction_order",
                        "language": "VI",
                        "elements": [
                            {
                                "attachment_id": "a-JJEvLdkcEPxTOwb6gYTfhwm26VSBHjaE3MDfrWedgLyC0smJRiA8w-csdGVg1cdxZLPT1je7k4i8nwbdYrSCJact3NOVGltEUQTjDayIhTvf1zqsR-Ai3aboRERgjvm-cI8iqv-NoIxi0cdNBoE6SYVJooM6xKTBft",
                                "type": "banner",
                            },
                            {
                                "type": "header",
                                "content": "Trạng thái đơn hàng",
                                "align": "left",
                            },
                            {
                                "type": "text",
                                "align": "left",
                                "content": "• Cảm ơn bạn đã mua hàng tại cửa hàng.<br>• Thông tin đơn hàng của bạn như sau:",
                            },
                            {
                                "type": "table",
                                "content": [
                                    {"value": "F-01332973223", "key": "Mã khách hàng"},
                                    {
                                        "style": "yellow",
                                        "value": "Đang giao",
                                        "key": "Trạng thái",
                                    },
                                    {"value": "250,000đ", "key": "Giá tiền"},
                                ],
                            },
                            {
                                "type": "text",
                                "align": "center",
                                "content": "📱Lưu ý điện thoại. Xin cảm ơn!",
                            },
                        ],
                        "buttons": [
                            {
                                "title": "Kiểm tra lộ trình - default icon",
                                "image_icon": "",
                                "type": "oa.open.url",
                                "payload": {"url": "https://oa.zalo.me/home"},
                            },
                            {
                                "title": "Xem lại giỏ hàng",
                                "image_icon": "wZ753VDsR4xWEC89zNTsNkGZr1xsPs19vZF22VHtTbxZ8zG9g24u3FXjZrQvQNH2wMl1MhbwT5_oOvX5_szXLB8tZq--TY0Dhp61JRfsAWglCej8ltmg3xC_rqsWAdjRkctG5lXzAGVlQe9BhZ9mJcSYVIDsc7MoPMnQ",
                                "type": "oa.query.show",
                                "payload": "kiểm tra giỏ hàng",
                            },
                            {
                                "title": "Liên hệ tổng đài",
                                "image_icon": "gNf2KPUOTG-ZSqLJaPTl6QTcKqIIXtaEfNP5Kv2NRncWPbDJpC4XIxie20pTYMq5gYv60DsQRHYn9XyVcuzu4_5o21NQbZbCxd087DcJFq7bTmeUq9qwGVie2ahEpZuLg2KDJfJ0Q12c85jAczqtKcSYVGJJ1cZMYtKR",
                                "type": "oa.open.phone",
                                "payload": {"phone_code": "84123456789"},
                            },
                        ],
                    },
                }
            },
        }

        response = requests.post(url, json=data, headers=headers)
        print(response.json())


if __name__ == "__main__":
    unittest.main()
