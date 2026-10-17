from enum import StrEnum

class ErrorBodyType(StrEnum):
    API_ERROR = "api_error"
    AUTHENTICATION_ERROR = "authentication_error"
    INVALID_REQUEST_ERROR = "invalid_request_error"
    PERMISSION_ERROR = "permission_error"
    RATE_LIMIT_ERROR = "rate_limit_error"

    def __str__(self) -> str:
        return str(self.value)
