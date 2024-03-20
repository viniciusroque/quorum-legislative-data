from data_models.base_data_model import BaseDataModel
from data_models.bills import Bill
from data_models.mapping_interface import MappingInterface
from pydantic import Field, dataclasses


class Vote(BaseDataModel):
    id: int
    bill_id: int
    bill: Bill

    def __str__(self):
        return f"{self.bill}"

    def __repr__(self):
        return f"({self.id}) {self.bill}"


@dataclasses.dataclass
class VoteMapping(MappingInterface[Vote]):
    votes: dict[int, Vote] = Field(default_factory=dict)

    def add(self, item: Vote) -> None:
        self.votes[item.id] =  item

    def get_by_id(self, id: int) -> Vote | None:
        try:
            return self.votes.get(int(id))
        except ValueError:
            return None

    def __str__(self) -> str:
        return f"{self.votes}"

    def __repr__(self) -> str:
        return f"{self.votes}"
