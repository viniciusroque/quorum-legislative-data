from pydantic import Field, dataclasses

from data_models.bills import Bill


@dataclasses.dataclass
class Vote:
    id: int
    bill_id: int
    bill: Bill

    def __str__(self):
        return f"{self.bill}"

    def __repr__(self):
        return f"({self.id}) {self.bill}"


@dataclasses.dataclass
class VoteMapping:
    votes: dict[int, Vote] = Field(default_factory=dict)

    def add(self, vote: Vote):
        self.votes.update({vote.id: vote})

    def get_by_id(self, id: int) -> Vote | None:
        return self.votes.get(int(id))

    def __str__(self):
        return f"{self.votes}"

    def __repr__(self):
        return f"{self.votes}"
