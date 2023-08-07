from zalo_sdk.oa.Client import Client
from zalo_sdk.oa.ZaloMessage import *

from . import ZaloSendMessage


class ZaloSendTextMessage(ZaloSendMessage):
    """
        read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-tu-van/gui-tin-tu-van-dang-van-ban
    """

    def test_send_text_message_body(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(text="Hello, world!")

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        body = client.create_request_body(recipient=recipient, body=message_body)

        data = {
            "recipient": {
                "user_id": self.user_id
            },
            "message": {
                "text": "Hello, world!"
            }
        }

        self.assertEqual(body, data)

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
        body = client.create_request_body(recipient=recipient, body=message_body)

        data = {
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
        self.assertEqual(body, data)

    def test_send_text_message_with_special_character(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(text=
        """
        🚀 New Arrival Alert 🚀
        Check out our latest collection now! Click the link below to explore our trendy products.
        ➡️ www.google.com
        """
        )

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        # Call the send_message function and assert the response
        body = client.create_request_body(recipient=recipient, body=message_body)

        data = {
            "recipient": {
                "user_id": self.user_id
            },
            "message": {
                "text":                     
                """
        🚀 New Arrival Alert 🚀
        Check out our latest collection now! Click the link below to explore our trendy products.
        ➡️ www.google.com
        """
            }
        }
        self.assertEqual(body, data)

    def test_send_text_message(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(text="Hello, world!")

        client = Client(self.app_id, self.secret_key, self.access_token, self.refresh_token)

        response = client.send_message(recipient=recipient, body=message_body, category='consultant')
        self.assertEqual(response["error"], 0)

    def test_send_text_message_with_invalid_access_token(self):
        recipient = ZaloRecipient(user_id=self.user_id)
        message_body = ZaloMessageBody(text="Hello, world!")

        client = Client(self.app_id, self.secret_key, "", self.refresh_token)

        # Call the send_message function and check if it raises an error
        with self.assertRaises(Exception) as context:
            client.send_message(recipient=recipient, body=message_body, category='consultant')

        # Check if the error code matches the expected -216
        self.assertEqual(context.exception.args[0], -216)
