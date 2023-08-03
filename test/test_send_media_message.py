import unittest
import requests


class ZaloSendMessage(unittest.TestCase):
    def setUp(self):
        # Set up the test data and objects if needed
        self.user_id = ""
        self.access_token = ""

    def test_send_message_media(self):
        """
        read more: https://developers.zalo.me/docs/official-account/tin-nhan/tin-truyen-thong/gui-tin-truyen-thong-ca-nhan
        """
        url = "https://openapi.zalo.me/v3.0/oa/message/promotion"

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
        response = requests.post(url, json=data, headers=headers)
        print(response.json())


if __name__ == "__main__":
    unittest.main()
