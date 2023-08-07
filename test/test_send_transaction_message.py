from zalo_sdk.oa.Client import Client
from zalo_sdk.oa.ZaloMessage import *

from . import ZaloSendMessage


class ZaloSendTransactionMessage(ZaloSendMessage):
    """
    read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-giao-dich/gui-tin-giao-dich
    """

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
        body = client.create_request_body(recipient=recipient, body=message_body)

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

        self.assertEqual(body, data)

    def test_send_transaction_message(self):
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
        response = client.send_message(recipient=recipient, body=message_body, category="transaction")

        
        self.assertEqual(response["error"], 0)

    def test_send_transaction_message_with_error_language(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            attachment=ZaloAttachment(
                payload_type="template",
                payload={
                        "template_type": "transaction_order",
                        "language": "ENG", # error language
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
        with self.assertRaises(Exception) as context:
            client.send_message(recipient=recipient, body=message_body, category="transaction")
        
        # Check if the error code matches the expected -201: language is invalid.
        self.assertEqual(context.exception.args[0], -201)
