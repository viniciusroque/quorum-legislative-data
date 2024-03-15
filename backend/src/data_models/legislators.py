from typing import Dict

from pydantic import Field, dataclasses


@dataclasses.dataclass
class Legislator:
    id: int
    name: str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}({self.id})"


@dataclasses.dataclass
class LegislatorMapping:
    legislators: Dict[int, Legislator] = Field(default_factory=dict)

    def add(self, legislator: Legislator):
        self.legislators.update({legislator.id: legislator})

    def get_by_id(self, id: int) -> Legislator | None:
        return self.legislators.get(int(id))

    def __str__(self):
        return f"{self.legislators}"

    def __repr__(self):
        return f"{self.legislators}"
