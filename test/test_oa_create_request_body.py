from zalo_sdk.oa.Client import Client
from zalo_sdk.oa.ZaloMessage import *

from . import ZaloSendMessage


class ZaloSendRequestBody(ZaloSendMessage):

    def test_send_text_message_body(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(text="Hello, world!")

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        generated_body = client.create_request_body(recipient=recipient, body=message_body)

        expected_body = {
            "recipient": {
                "user_id": self.user_id
            },
            "message": {
                "text": "Hello, world!"
            }
        }

        self.assertEqual(generated_body, expected_body)

    def test_send_long_text_message_body(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(text=
            """
            Hello 👋,

            Welcome to our store! 🛍️

            We have a special promotion going on right now! 🎉

            📣 Don't miss out on these amazing deals:
            1. 50% OFF on all items 🎁
            2. Buy 2, Get 1 Free 🎈
            3. Free Shipping on orders over $50 🚚

            🔥 Hurry up and shop now before the offer ends!

            💬 Need help or have any questions? Feel free to reach out to our customer support team. We're here to assist you 24/7.

            📞 Call us at +1 (800) 123-4567 or send us a message through our website.

            Thank you for choosing us. We hope you have a wonderful shopping experience!

            Best regards,
            Your Store Team 🛒

            """
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        generated_body = client.create_request_body(recipient=recipient, body=message_body)

        expected_body = {
            "recipient": {
                "user_id": self.user_id
            },
            "message": {
                "text":             
                """
            Hello 👋,

            Welcome to our store! 🛍️

            We have a special promotion going on right now! 🎉

            📣 Don't miss out on these amazing deals:
            1. 50% OFF on all items 🎁
            2. Buy 2, Get 1 Free 🎈
            3. Free Shipping on orders over $50 🚚

            🔥 Hurry up and shop now before the offer ends!

            💬 Need help or have any questions? Feel free to reach out to our customer support team. We're here to assist you 24/7.

            📞 Call us at +1 (800) 123-4567 or send us a message through our website.

            Thank you for choosing us. We hope you have a wonderful shopping experience!

            Best regards,
            Your Store Team 🛒

            """
            }
        }
        self.assertEqual(generated_body, expected_body)


    def test_send_transaction_message_body(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            attachment=ZaloAttachment(
                payload_type="template",
                payload={
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
            )
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        generated_body = client.create_request_body(recipient=recipient, body=message_body)

        expected_body = {
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

        self.assertEqual(generated_body, expected_body)


    def test_send_sticker_message_body(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            attachment=ZaloAttachment(
                payload_type="template",
                payload={
                    "template_type": "media",
                    "elements": [
                        {
                            "media_type": "sticker",
                            "attachment_id": "bfe458bf64fa8da4d4eb",
                        }
                    ],
                }
            )
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        generated_body = client.create_request_body(recipient=recipient, body=message_body)

        expected_body = {
            "recipient": {"user_id": self.user_id},
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "media",
                        "elements": [
                            {
                                "media_type": "sticker",
                                "attachment_id": "bfe458bf64fa8da4d4eb",
                            }
                        ],
                    },
                }
            },
        }

        self.assertEqual(generated_body, expected_body)


    def test_send_request_form_message_body(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            attachment=ZaloAttachment(
                payload_type="template",
                payload={
                        "template_type": "request_user_info",
                        "elements": [
                            {
                                "title": "OA Chatbot (Testing)",
                                "subtitle": "Đang yêu cầu thông tin từ bạn",
                                "image_url": "https://developers.zalo.me/web/static/zalo.png",
                            }
                        ],
                    },
            )
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        generated_body = client.create_request_body(recipient=recipient, body=message_body)

        expected_body = {
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

        self.assertEqual(generated_body, expected_body)


    def test_send_reply_message_body(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            text= "Chào bạn, Shop có địa chỉ là 182 Lê Đại Hành, P15, Q10, HCM",
            quote_message_id=self.quote_message_id
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        generated_body = client.create_request_body(recipient=recipient, body=message_body)

        expected_body = {
            "recipient": {
                "user_id": self.user_id
            },
            "message": {
                "text": "Chào bạn, Shop có địa chỉ là 182 Lê Đại Hành, P15, Q10, HCM",
                "quote_message_id": self.quote_message_id
            }
        }

        self.assertEqual(generated_body, expected_body)


    def test_send_media_message_body(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            attachment=ZaloAttachment(
                payload_type="template",
                payload={
                        "template_type": "promotion",
                        "elements": [
                            {
                                "attachment_id": "aERC3A0iYGgQxim8fYIK6fxzsXkaFfq7ZFRB3RCyZH6RyziRis3RNydebK3iSPCJX_cJ3k1nW1EQufjN_pUL1f6Ypq3rTef5nxp6H_HnXKFDiyD5y762HS-baqRpQe5FdA376lTfq1sRyPr8ypd74ecbaLyA-tGmuJ-97W",
                                "type": "banner",
                            },
                            {
                                "type": "header",
                                "content": "💥💥Ưu đãi thành viên Platinum💥💥",
                            },
                            {
                                "type": "text",
                                "align": "left",
                                "content": "Ưu đãi dành riêng cho khách hàng Nguyen Van A hạng thẻ Platinum<br>Voucher trị giá 150$",
                            },
                            {
                                "type": "table",
                                "content": [
                                    {"value": "VC09279222", "key": "Voucher"},
                                    {"value": "30/12/2023", "key": "Hạn sử dụng"},
                                ],
                            },
                            {
                                "type": "text",
                                "align": "center",
                                "content": "Áp dụng tất cả cửa hàng trên toàn quốc",
                            },
                        ],
                        "buttons": [
                            {
                                "title": "Tham khảo chương trình",
                                "image_icon": "",
                                "type": "oa.open.url",
                                "payload": {"url": "https://oa.zalo.me/home"},
                            },
                            {
                                "title": "Liên hệ chăm sóc viên",
                                "image_icon": "aeqg9SYn3nIUYYeWohGI1fYRF3V9f0GHceig8Ckq4WQVcpmWb-9SL8JLPt-6gX0QbTCfSuQv40UEst1imAm53CwFPsQ1jq9MsOnlQe6rIrZOYcrlWBTAKy_UQsV9vnfGozCuOvFfIbN5rcXddFKM4sSYVM0D50I9eWy3",
                                "type": "oa.query.hide",
                                "payload": "#tuvan",
                            },
                        ],
                    }
            )
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        generated_body = client.create_request_body(recipient=recipient, body=message_body)

        expected_body = {
            "recipient": {"user_id": self.user_id},
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "promotion",
                        "elements": [
                            {
                                "attachment_id": "aERC3A0iYGgQxim8fYIK6fxzsXkaFfq7ZFRB3RCyZH6RyziRis3RNydebK3iSPCJX_cJ3k1nW1EQufjN_pUL1f6Ypq3rTef5nxp6H_HnXKFDiyD5y762HS-baqRpQe5FdA376lTfq1sRyPr8ypd74ecbaLyA-tGmuJ-97W",
                                "type": "banner",
                            },
                            {
                                "type": "header",
                                "content": "💥💥Ưu đãi thành viên Platinum💥💥",
                            },
                            {
                                "type": "text",
                                "align": "left",
                                "content": "Ưu đãi dành riêng cho khách hàng Nguyen Van A hạng thẻ Platinum<br>Voucher trị giá 150$",
                            },
                            {
                                "type": "table",
                                "content": [
                                    {"value": "VC09279222", "key": "Voucher"},
                                    {"value": "30/12/2023", "key": "Hạn sử dụng"},
                                ],
                            },
                            {
                                "type": "text",
                                "align": "center",
                                "content": "Áp dụng tất cả cửa hàng trên toàn quốc",
                            },
                        ],
                        "buttons": [
                            {
                                "title": "Tham khảo chương trình",
                                "image_icon": "",
                                "type": "oa.open.url",
                                "payload": {"url": "https://oa.zalo.me/home"},
                            },
                            {
                                "title": "Liên hệ chăm sóc viên",
                                "image_icon": "aeqg9SYn3nIUYYeWohGI1fYRF3V9f0GHceig8Ckq4WQVcpmWb-9SL8JLPt-6gX0QbTCfSuQv40UEst1imAm53CwFPsQ1jq9MsOnlQe6rIrZOYcrlWBTAKy_UQsV9vnfGozCuOvFfIbN5rcXddFKM4sSYVM0D50I9eWy3",
                                "type": "oa.query.hide",
                                "payload": "#tuvan",
                            },
                        ],
                    },
                }
            },
        }

        self.assertEqual(generated_body, expected_body)


    def test_send_image_message_body(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            text="Zalo đạt 100 triệu người dùng",
            attachment=ZaloAttachment(
                payload_type="template",
                payload={
                    "template_type": "media",
                    "elements": [
                        {
                            "media_type": "image",
                            "url": "https://stc-developers.zdn.vn/images/bg_1.jpg",
                        }
                    ],
                },
            )
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        generated_body = client.create_request_body(recipient=recipient, body=message_body)

        expected_body = {
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

        self.assertEqual(generated_body, expected_body)

    def test_send_action_message_body(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloAction(
            react_icon = "/-strong",
            react_message_id= "d38a3d9e89585f02064d",
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        generated_body = client.create_request_body(recipient=recipient, action=message_body)

        expected_body = {
            "recipient": {
                "user_id": self.user_id
            },
            "sender_action": {
                "react_icon": "/-strong",
                "react_message_id": "d38a3d9e89585f02064d"
            }
        }

        self.assertEqual(generated_body, expected_body)
