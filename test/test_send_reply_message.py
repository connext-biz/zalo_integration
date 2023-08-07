from zalo_sdk.oa.Client import Client
from zalo_sdk.oa.ZaloMessage import *

from . import ZaloSendMessage


class ZaloSendReplyMessage(ZaloSendMessage):
    """
        read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-tu-van/gui-tin-tu-van-dang-van-ban
    """

    def test_send_reply_message_body(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            text= "Chào bạn, Shop có địa chỉ là 182 Lê Đại Hành, P15, Q10, HCM",
            quote_message_id=self.quote_message_id
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        body = client.create_request_body(recipient=recipient, body=message_body)

        data = {
            "recipient": {
                "user_id": self.user_id
            },
            "message": {
                "text": "Chào bạn, Shop có địa chỉ là 182 Lê Đại Hành, P15, Q10, HCM",
                "quote_message_id": self.quote_message_id
            }
        }

        self.assertEqual(body, data)

    def test_send_reply_message(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            text= "Chào bạn, Shop có địa chỉ là 182 Lê Đại Hành, P15, Q10, HCM",
            quote_message_id=self.quote_message_id
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        response = client.send_message(recipient=recipient, body=message_body, category='consultant')
        self.assertEqual(response["error"], 0)

    def test_send_reply_message_with_no_quote_message_id(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            text= "Chào bạn, Shop có địa chỉ là 182 Lê Đại Hành, P15, Q10, HCM",
            quote_message_id=""
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        response = client.send_message(recipient=recipient, body=message_body, category='consultant')
        self.assertEqual(response["error"], 0)

    def test_send_reply_message_with_wrong_quote_message_id(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(
            text= "Chào bạn, Shop có địa chỉ là 182 Lê Đại Hành, P15, Q10, HCM",
            quote_message_id="4365821274504019135" # quote_message_id does not exist
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        response = client.send_message(recipient=recipient, body=message_body, category='consultant')
        self.assertEqual(response["error"], 0)


    

    



