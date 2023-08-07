from zalo_sdk.oa.Client import Client
from zalo_sdk.oa.ZaloMessage import *

from . import ZaloSendMessage


class ZaloSendMediaMessage(ZaloSendMessage):
    """
    read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-truyen-thong/gui-tin-truyen-thong-ca-nhan
    """

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
        body = client.create_request_body(recipient=recipient, body=message_body)

        data = {
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

        self.assertEqual(body, data)

    def test_send_media_message(self):
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
        response = client.send_message(recipient=recipient, body=message_body, category='media')



        self.assertEqual(response["error"], 0)

    def test_send_media_message_with_error_type(self):
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

        # Call the send_message function and check if it raises an error
        with self.assertRaises(Exception) as context:
            client.send_message(recipient=recipient, body=message_body, category='consultant')

        # Check if the error code matches the expected -233: message type is invalid or not support
        self.assertEqual(context.exception.args[0], -233)


    def test_send_media_message_with_out_of_quota(self):
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

        # Call the send_message function and check if it raises an error
        with self.assertRaises(Exception) as context:
            client.send_message(recipient=recipient, body=message_body, category='media')

        # Check if the error code matches the expected -218: The user is out of quota receive.
        self.assertEqual(context.exception.args[0], -218)
