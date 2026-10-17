from enum import StrEnum

class MatchSearchResultObject(StrEnum):
    MATCH_SEARCH = "match_search"

    def __str__(self) -> str:
        return str(self.value)
