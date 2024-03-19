from data_models.base_data_model import BaseDataModel
from data_models.legislators import Legislator
from data_models.mapping_interface import MappingInterface
from pydantic import Field, dataclasses


@dataclasses.dataclass
class Bill(BaseDataModel):
    id: int
    title: str
    sponsor_id: int
    primary_sponsor: Legislator

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"{self.title}({self.id})"


@dataclasses.dataclass
class BillMapping(MappingInterface[Bill]):
    bills: dict[int, Bill] = Field(default_factory=dict)

    def add(self, item: Bill) -> None:
        self.bills.update({item.id: item})

    def get_by_id(self, id: int) -> Bill | None:
        try:
            return self.bills.get(int(id))
        except ValueError:
            return None

    def __str__(self) -> str:
        return f"{self.bills}"

    def __repr__(self) -> str:
        return f"{self.bills}"
