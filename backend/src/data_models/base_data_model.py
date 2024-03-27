import pydantic


class BaseDataModel(pydantic.BaseModel):

    id: int
