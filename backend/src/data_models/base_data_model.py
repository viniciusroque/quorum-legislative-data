from abc import ABC

from pydantic import dataclasses


@dataclasses.dataclass
class BaseDataModel(ABC):

    id: int
