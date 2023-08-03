import unittest
import requests

class TestFileUpload(unittest.TestCase):
    def setUp(self):
        self.access_token = ""
        self.upload_url = "https://openapi.zalo.me/v2.0/oa/upload/file"
        self.file_path = ""

    def test_file_upload(self):
        """
        read more about file upload here: https://developers.zalo.me/docs/official-account/tin-nhan/quan-ly-tin-nhan/upload-hinh-anh
        """
        headers = {
            "access_token": self.access_token
        }

        files = {
            "file": open(self.file_path, "rb")
        }

        response = requests.post(self.upload_url, headers=headers, files=files)
        data = response.json()
        print(data)

if __name__ == "__main__":
    unittest.main()
