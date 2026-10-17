from enum import StrEnum

class MatchListObject(StrEnum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
