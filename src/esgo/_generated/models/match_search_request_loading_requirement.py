from enum import StrEnum

class MatchSearchRequestLoadingRequirement(StrEnum):
    ANY = "any"
    HECK = "heck"
    OBEN = "oben"
    SEITE = "seite"

    def __str__(self) -> str:
        return str(self.value)
