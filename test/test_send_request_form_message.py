from zalo_sdk.oa.Client import Client
from zalo_sdk.oa.ZaloMessage import *

from . import ZaloSendMessage


class ZaloSendRequestFormMessage(ZaloSendMessage):
    """
    read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-tu-van/gui-tin-tu-van-theo-mau-yeu-cau-thong-tin-nguoi-dung
    """

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
        body = client.create_request_body(recipient=recipient, body=message_body)

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

        self.assertEqual(body, data)

    def test_send_request_form_message(self):
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
        response = client.send_message(recipient=recipient, body=message_body)

        

        self.assertEqual(response["error"], 0)


    def test_send_request_form_message_with_error_template_type(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            attachment=ZaloAttachment(
                payload_type="template",
                payload={
                        "template_type": "request_user_information", # error template_type
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

        # Call the send_message function and check if it raises an error
        with self.assertRaises(Exception) as context:
            client.send_message(recipient=recipient, body=message_body, category='media')

        # Check if the error code matches the expected -201: Missing template_type params.
        self.assertEqual(context.exception.args[0], -201)

