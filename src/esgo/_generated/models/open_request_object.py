from enum import StrEnum

class OpenRequestObject(StrEnum):
    OPEN_REQUEST = "open_request"

    def __str__(self) -> str:
        return str(self.value)
