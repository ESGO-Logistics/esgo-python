from enum import StrEnum

class MatchObject(StrEnum):
    MATCH = "match"

    def __str__(self) -> str:
        return str(self.value)
