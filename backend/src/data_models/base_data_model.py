from abc import ABC
import pydantic


class BaseDataModel(pydantic.BaseModel, ABC):

    id: int
