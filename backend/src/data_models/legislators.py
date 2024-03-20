from annotated_types import Le
from data_models.base_data_model import BaseDataModel
from data_models.mapping_interface import MappingInterface
from pydantic import Field, dataclasses


class Legislator(BaseDataModel):
    id: int
    name: str

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}({self.id})"


@dataclasses.dataclass
class LegislatorMapping(MappingInterface[Legislator]):
    legislators: dict[int, Legislator] = Field(default_factory=dict)

    def add(self, item: Legislator) -> None:
        self.legislators[item.id] = item

    def get_by_id(self, id: int) -> Legislator | None:
        try:
            return self.legislators.get(int(id))
        except ValueError:
            return None

    def __str__(self):
        return f"{self.legislators}"

    def __repr__(self):
        return f"{self.legislators}"
