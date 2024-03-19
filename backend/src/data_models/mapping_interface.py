import abc
from typing import Generic, TypeVar

from data_models.base_data_model import BaseDataModel

T = TypeVar("T", bound=BaseDataModel)


class MappingInterface(Generic[T], abc.ABC):

    @abc.abstractmethod
    def get_by_id(self, id: int) -> T | None:
        raise NotImplementedError("You must implement the get_by_id method")

    @abc.abstractmethod
    def add(self, item: T) -> None:
        raise NotImplementedError("You must implement the add method")
