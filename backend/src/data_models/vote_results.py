import enum

from pydantic import dataclasses

from data_models.legislators import Legislator
from data_models.votes import Vote


class VoteType(int, enum.Enum):
    YEA = 1
    NAY = 2


@dataclasses.dataclass
class VoteResult:
    id: int
    legislator: Legislator
    vote: Vote
    vote_type: VoteType

    @property
    def vote_type_key(self) -> int:
        return self.vote_type.value

    def __str__(self):
        return f"{self.legislator} ({self.legislator.id}): voted {self.vote_type} on {self.vote} ({self.vote.id})"

    def __repr__(self):
        return f"{self.legislator.id} voted type {self.vote_type.value} on {self.vote.id} / bill {self.vote.bill.id}"
