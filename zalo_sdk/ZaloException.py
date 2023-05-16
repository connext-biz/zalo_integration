class ZaloException(Exception):
    def __init__(self, code, custom_message=None):
        self._code = code
        self._custom_message = custom_message
        self._msg = f"Zalo error ({self._code})"
        if custom_message is not None:
            self._msg += f": {custom_message}"

    def __str__(self) -> str:
        return self._msg