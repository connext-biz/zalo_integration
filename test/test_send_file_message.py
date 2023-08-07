from zalo_sdk.oa.Client import Client
from zalo_sdk.oa.ZaloMessage import *

from . import ZaloSendMessage


class ZaloSendFileMessage(ZaloSendMessage):
    """
        read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-tu-van/gui-tin-tu-van-dang-van-ban
    """

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
        body = client.create_request_body(recipient=recipient, body=message_body)

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

        self.assertEqual(body, data)

    def test_send_image_message(self):
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
        response = client.send_message(recipient=recipient, body=message_body)

        self.assertEqual(response["error"], 0)


    def test_send_file_message_body(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            attachment=ZaloAttachment(
                payload_type="file",
                payload={"token": ""},
            )
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        body = client.create_request_body(recipient=recipient, body=message_body)

        data = {
            "recipient": {"user_id": self.user_id},
            "message": {
                "attachment": {
                    "type": "file",
                    "payload": {
                        "token": ""
                    },
                }
            },
        }

        self.assertEqual(body, data)
