from pydantic import dataclasses

from data_models.legislators import Legislator
from data_models.vote_results import VoteType


@dataclasses.dataclass
class LegislatorVoteType:
    legislator: Legislator
    vote_type: VoteType

    def __str__(self):
        return f"{self.legislator}"

    def __repr__(self):
        return f"{self.legislator} voted {self.vote_type}"
