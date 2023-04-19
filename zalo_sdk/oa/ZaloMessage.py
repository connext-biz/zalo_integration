import enum


class ZaloMessage:
    def __init__(self, recipient=None, message_body=None, action=None):
        """
        Parameters:
        recipients (ZaloRecipient): Recipients of the message
        message_body (ZaloMessageBody): Message body
        action (ZaloAction): send an action (e.g. emoji react)
        """
        self.msg = {}
        self.msg["recipient"] = recipient
        self.msg["message"] = message_body
        self.msg["sender_action"] = action

    def toDict(self) -> dict:
        return {k: v.toDict() for k, v in dict(filter(lambda pair: pair[1] is not None, self.msg.items())).items()}


class ZaloPayloadType(enum.Enum):
    file = enum.auto()
    template = enum.auto()


class ZaloTemplateType(enum.Enum):
    media = enum.auto()
    list = enum.auto()
    request_user_info = enum.auto()


class ZaloAttachment:
    def __init__(self, payload_type: ZaloPayloadType, payload):
        self.payload_type = payload_type
        self.payload = payload

    def toDict(self) -> dict:
        return {
            "type": self.payload_type.name,
            "payload": self.payload.toDict()
        }


class ZaloMessageBody:
    def __init__(self, text: str = None, attachment: ZaloAttachment = None):
        self.body = {}
        self.body["text"] = text
        self.body["attachment"] = attachment

    def toDict(self) -> dict:
        return {k: v if isinstance(v, str) else v.toDict() for k, v in dict(filter(lambda pair: pair[1] is not None, self.body.items())).items()}


class ZaloRecipient:
    def __init__(self, message_id=None, user_id=None, target=None):
        """
        Define a list of recipients. If more than one param is provided, only one is used.
        The priority order is

        message_id > user_id > target

        Parameters:
        user_id (str): When set, send a message directly to a user
        message_id (str): When set, send a direct response to user. More information,
                see https://developers.zalo.me/docs/api/official-account-api/gui-tin-va-thong-bao-qua-oa/gui-lenh-phan-hoi-nguoi-dung-post-5027
        target (dict): When set, send a broadcast message to targeted users. For more user targetting parameters
                see https://developers.zalo.me/docs/api/official-account-api/gui-tin-va-thong-bao-qua-oa/broadcast-bai-viet-post-5021
        """
        self.user_id = user_id
        self.message_id = message_id
        self.target = target

    def toDict(self) -> dict:
        """
        Convert the object to dict. If there is more than one parameter set, only
        one parameter is use. The priority is
        message_id > user_id > target
        """

        if self.message_id is not None:
            return {"message_id": self.message_id}
        elif self.user_id is not None:
            return {"user_id": self.user_id}
        elif self.target is not None:
            return {"target": self.target}
        else:
            return {}


class ZaloAction:
    """
    Send react emoji to user

    For more information, see
    https://developers.zalo.me/docs/api/official-account-api/gui-tin-va-thong-bao-qua-oa/tha-bieu-tuong-cam-xuc-vao-tin-nhan-post-6183
    """

    def __init__(self, react_icon, react_message_id):
        self.react_icon = react_icon
        self.react_message_id = react_message_id

    def toDict(self) -> dict:
        return {
            "react_icon": self.react_icon,
            "react_message_id": self.react_message_id
        }


class ZaloTemplateElement:
    def __init__(self, **kwargs):
        self.elem = {}
        self.elem["media_type"] = kwargs.get("media_type", None)
        self.elem["url"] = kwargs.get("url", None)
        self.elem["title"] = kwargs.get("title", None)
        self.elem["subtitle"] = kwargs.get("subtitle", None)
        self.elem["image_url"] = kwargs.get("image_url", None)
        self.elem["default_action"] = kwargs.get("default_action", None)

    def toDict(self):

        print(
            f"elem: {dict(filter(lambda pair: pair[1] is not None, self.elem.items()))}")
        return dict(filter(lambda pair: pair[1] is not None, self.elem.items()))


class ZaloAttachmentTemplate:
    def __init__(self, template_type: ZaloTemplateType, elements: list, buttons: list):
        self.template_type = template_type
        self.elements = elements
        self.buttons = buttons

    def toDict(self) -> dict:
        result = {
            "template_type": self.template_type.name,

            "buttons": []
        }

        if self.elements is not None and len(self.elements) > 0:
            result["elements"] = []
            for e in self.elements:
                result["elements"].append(e.toDict())

        if self.buttons is not None and len(self.buttons) > 0:
            result["buttons"] = []
            for b in self.buttons:
                result["buttons"].append(e.toDict())

        return result


class ZaloAttachmentFile:
    """
    Used for sending files to users as attachment. This object has a payload token
    returned from file upload API.

    See https://developers.zalo.me/docs/api/official-account-api/upload-hinh-anh/upload-file-post-5087
    for more information about uploading file. 
    """

    def __init__(self, payload_token):
        self.payload = payload_token

    def toDict(self) -> dict:
        return {
            "payload": self.payload
        }
