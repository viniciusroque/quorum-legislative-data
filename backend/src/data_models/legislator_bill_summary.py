from collections import defaultdict
from pydantic import Field, dataclasses

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


@dataclasses.dataclass
class VoteTypeCounter:
    vote_type_count_by_legislator: dict[int, dict[int, int]] = Field(
        default_factory=lambda: defaultdict(lambda: defaultdict(int))
    )

    def increment_vote_type_count(self, legislator_id: int, vote_type_key: int):
        self.vote_type_count_by_legislator[legislator_id][vote_type_key] += 1

    def get_vote_type_count(self):
        return dict(self.vote_type_count_by_legislator)
