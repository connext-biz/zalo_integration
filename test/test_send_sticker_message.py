from zalo_sdk.oa.Client import Client
from zalo_sdk.oa.ZaloMessage import *

from . import ZaloSendMessage


class ZaloSendStickerMessage(ZaloSendMessage):
    """
    read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-tu-van/gui-tin-tu-van-kem-sticker
    """

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
        body = client.create_request_body(recipient=recipient, body=message_body)

        data = {
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

        self.assertEqual(body, data)

    def test_send_sticker_message(self):
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
        response = client.send_message(recipient=recipient, body=message_body)

        self.assertEqual(response["error"], 0)

    def test_send_sticker_message_with_error_sticker_id(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            attachment=ZaloAttachment(
                payload_type="template",
                payload={
                    "template_type": "media",
                    "elements": [
                        {
                            "media_type": "sticker",
                            "attachment_id": "bfe458bf64fa8da4d4ea", # wrong sticker id
                        }
                    ],
                }
            )
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and check if it raises an error
        with self.assertRaises(Exception) as context:
            client.send_message(recipient=recipient, body=message_body, category='consultant')

        # Check if the error code matches the expected -201: stickerid is not valid.
        self.assertEqual(context.exception.args[0], -201)
