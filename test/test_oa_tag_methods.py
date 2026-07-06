from unittest.mock import Mock

from zalo_sdk.oa.Client import Client

from . import ZaloSendMessage


class ZaloOATagMethods(ZaloSendMessage):

    def _create_client(self):
        return Client(
            self.app_id,
            self.secret_key,
            access_token="access-token",
            refresh_token=self.refresh_token,
            endpoint_prefix="https://test.openapi.zalo.me",
        )

    def _mock_client_response(self, client):
        raw_response = Mock()
        validated_response = {
            "error": 0,
            "message": "Success",
        }
        client.send_request = Mock(return_value=raw_response)
        client._validate_zalo_response = Mock(return_value=validated_response)

        return raw_response, validated_response

    def test_tag_follower_posts_expected_request(self):
        client = self._create_client()
        raw_response, validated_response = self._mock_client_response(client)

        result = client.tag_follower(
            user_id="2468458835296197922",
            tag_name="Khach hang mua lan dau",
        )

        client.send_request.assert_called_once_with(
            method="POST",
            url="https://test.openapi.zalo.me/v2.0/oa/tag/tagfollower",
            body={
                "user_id": "2468458835296197922",
                "tag_name": "Khach hang mua lan dau",
            },
            headers={
                "Content-Type": "application/json",
                "access_token": "access-token",
            },
        )
        client._validate_zalo_response.assert_called_once_with(raw_response)
        self.assertEqual(result, validated_response)

    def test_rm_follower_from_tag_posts_expected_request(self):
        client = self._create_client()
        raw_response, validated_response = self._mock_client_response(client)

        result = client.rm_follower_from_tag(
            user_id="2468458835296197922",
            tag_name="Khach hang mua lan dau",
        )

        client.send_request.assert_called_once_with(
            method="POST",
            url="https://test.openapi.zalo.me/v2.0/oa/tag/rmfollowerfromtag",
            body={
                "user_id": "2468458835296197922",
                "tag_name": "Khach hang mua lan dau",
            },
            headers={
                "Content-Type": "application/json",
                "access_token": "access-token",
            },
        )
        client._validate_zalo_response.assert_called_once_with(raw_response)
        self.assertEqual(result, validated_response)

    def test_get_tags_of_oa_gets_expected_request(self):
        client = self._create_client()
        raw_response = Mock()
        validated_response = {
            "data": ["Khach Q1", "Khach Q2"],
            "error": 0,
            "message": "Success",
        }
        client.send_request = Mock(return_value=raw_response)
        client._validate_zalo_response = Mock(return_value=validated_response)

        result = client.get_tags_of_oa()

        client.send_request.assert_called_once_with(
            method="GET",
            url="https://test.openapi.zalo.me/v2.0/oa/tag/gettagsofoa",
            headers={
                "access_token": "access-token",
            },
        )
        client._validate_zalo_response.assert_called_once_with(raw_response)
        self.assertEqual(result, validated_response)

    def test_rm_tag_posts_expected_request(self):
        client = self._create_client()
        raw_response, validated_response = self._mock_client_response(client)

        result = client.rm_tag(tag_name="Khach hang mua lan dau")

        client.send_request.assert_called_once_with(
            method="POST",
            url="https://test.openapi.zalo.me/v2.0/oa/tag/rmtag",
            body={
                "tag_name": "Khach hang mua lan dau",
            },
            headers={
                "Content-Type": "application/json",
                "access_token": "access-token",
            },
        )
        client._validate_zalo_response.assert_called_once_with(raw_response)
        self.assertEqual(result, validated_response)
