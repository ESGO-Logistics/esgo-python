from enum import StrEnum

class MeObject(StrEnum):
    ME = "me"

    def __str__(self) -> str:
        return str(self.value)
