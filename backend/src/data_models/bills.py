from pydantic import Field, dataclasses

from data_models.legislators import Legislator


@dataclasses.dataclass
class Bill:
    id: int
    title: str
    sponsor_id: int
    primary_sponsor: Legislator

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"{self.title}({self.id})"


@dataclasses.dataclass
class BillMapping:
    bills: dict[int, Bill] = Field(default_factory=dict)

    def add(self, bill: Bill):
        self.bills.update({bill.id: bill})

    def get_by_id(self, id: int) -> Bill | None:
        return self.bills.get(int(id))

    def __str__(self):
        return f"{self.bills}"

    def __repr__(self):
        return f"{self.bills}"
