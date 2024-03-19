import enum

from pydantic import dataclasses

from data_models.base_data_model import BaseDataModel
from data_models.legislators import Legislator
from data_models.votes import Vote


class VoteType(int, enum.Enum):
    YEA = 1
    NAY = 2


@dataclasses.dataclass
class VoteResult(BaseDataModel):
    id: int
    legislator_id: int
    legislator: Legislator
    vote_id: int
    vote: Vote
    vote_type: VoteType

    def __str__(self):
        return f"{self.legislator} ({self.legislator.id}): voted {self.vote_type} on {self.vote} ({self.vote.id})"

    def __repr__(self):
        return f"{self.legislator.id} voted type {self.vote_type.value} on {self.vote.id} / bill {self.vote.bill.id}"
