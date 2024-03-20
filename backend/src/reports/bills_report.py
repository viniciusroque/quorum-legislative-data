from collections import defaultdict

from data_models.bills import Bill
from data_models.vote_results import VoteResult, VoteType
from pydantic import Field, dataclasses
from reports.base_processors import BaseProcessor


@dataclasses.dataclass
class BillVotes:
    supporters: set[int] = Field(default_factory=set)
    opposers: set[int] = Field(default_factory=set)

    @property
    def count_supporters(self) -> int:
        return len(self.supporters)

    @property
    def count_opposers(self) -> int:
        return len(self.opposers)

    def __str__(self):
        return f"Supported: {self.supporters} / Opposed: {self.opposers}"

    def __repr__(self):
        return f"Supported: {self.supporters} / Opposed: {self.opposers}"


@dataclasses.dataclass
class BillsReport(BaseProcessor):
    bill_votes: dict[int, BillVotes] = Field(
        default_factory=lambda: defaultdict(BillVotes)
    )
    bills_mapping: dict[int, Bill] = Field(default_factory=dict)

    def process_vote_result(self, vote_result: VoteResult):
        if vote_result.vote_type == VoteType.YEA:
            self.bill_votes[vote_result.vote.bill.id].supporters.add(
                vote_result.legislator.id
            )
        else:
            self.bill_votes[vote_result.vote.bill.id].opposers.add(
                vote_result.legislator.id
            )

        self.bills_mapping[vote_result.vote.bill.id] = vote_result.vote.bill
