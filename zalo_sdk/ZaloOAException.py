import zalo_sdk


class ZaloOAException(zalo_sdk.ZaloException):
    """
    Zalo Official Account specific exception.

    Official document for the error codes:
    https://developers.zalo.me/docs/api/official-account-api/phu-luc/ma-loi-post-735
    """
    ERROR_CODE_TO_STR = {
        0: "Success",
        -32: "Rate limited",
        -201: "Invalid parameters",
        -202: "Invalid Mac",
        -204: "Official Account has been deleted",
        -205: "Non-exitance Official Account",
        -207: "Official Account has not been registered as a 3rd party",
        -208: "Official Account does not have secret key",
        -209: "Not supported API",
        -210: "Parameter outside permitted range",
        -211: "Out of quota",
        -212: "API has not been registered with this Official Account",
        -213: "User has not follow this Official Account",
        -214: "Article is being processing",
        -215: "Invalid App ID",
        -216: "Invalid Access Token",
        -217: "User blocked invitation to follow",
        -218: "Out of quota for receiving",
        -221: "Official Account has not been authenticated",
        -222: "User account has been blocked or not active for more than 45 days",
        -224: "Official Account has not subscribe to the service package",
        -227: "User account has been blocked or not active for more than 45 days",
        -230: "User has not interacted with the OA in the past 7 days",
        -233: "Message type is invalid or not support",
        -305: "Offical Account cannot response to user after 48 hours",
        -311: "Out of quota for responding to user message",
        -320: "Application needs to link with Zalo Business Account to use paid features",
        -321: "Zalo Business Account linked with the Application is low on balance or cannot make payment"
    }

    def __init__(self, code, custom_message=None):
        super(ZaloOAException, self).__init__(code, custom_message)
        self._msg = f"Zalo OA error ({self._code}) [{self.errCodeToStr()}]"
        if custom_message is not None:
            self._msg += f": {custom_message}"

    def errCodeToStr(self) -> str:
        if self._code in ZaloOAException.ERROR_CODE_TO_STR:
            return ZaloOAException.ERROR_CODE_TO_STR[self._code]

        return "Unknown error"


class ZaloOAAuthTokenExpiredException(ZaloOAException):
    """
    Auth token expired expcetion. When we get this exception, we should
    refresh the auth token to get a new one.
    """
    pass
