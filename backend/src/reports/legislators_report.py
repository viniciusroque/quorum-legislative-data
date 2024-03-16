from collections import defaultdict
from multiprocessing.process import BaseProcess
from data_models.bills import Bill
from data_models.legislators import Legislator
from data_models.vote_results import VoteResult, VoteType
from pydantic import Field, dataclasses


@dataclasses.dataclass
class LegislatorVotes:
    supported_bills: set[int] = Field(default_factory=set)
    opposed_bills: set[int] = Field(default_factory=set)

    def __str__(self):
        return f"Supported: {self.supported_bills} / Opposed: {self.opposed_bills}"

    def __repr__(self):
        return f"Supported: {self.supported_bills} / Opposed: {self.opposed_bills}"

    @property
    def count_supported_bills(self) -> int:
        return len(self.supported_bills)

    @property
    def count_opposed_bills(self) -> int:
        return len(self.opposed_bills)


@dataclasses.dataclass
class LegislatorsReport(BaseProcess):

    legislators_votes: dict[int, LegislatorVotes] = Field(
        default_factory=lambda: defaultdict(LegislatorVotes)
    )
    bills_mapping: dict[int, Bill] = Field(default_factory=dict)
    legislator_mapping: dict[int, Legislator] = Field(default_factory=dict)

    def process_vote_result(self, vote_result: VoteResult):
        if vote_result.vote_type == VoteType.YEA:
            self.legislators_votes[vote_result.legislator.id].supported_bills.add(
                vote_result.vote.bill.id
            )
        else:
            self.legislators_votes[vote_result.legislator.id].opposed_bills.add(
                vote_result.vote.bill.id
            )

        self.bills_mapping[vote_result.vote.bill.id] = vote_result.vote.bill
        self.legislator_mapping[vote_result.legislator.id] = vote_result.legislator
