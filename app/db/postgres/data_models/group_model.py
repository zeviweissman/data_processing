from pydantic import BaseModel, Field

class GroupModel(BaseModel):
    id: int = Field(default=0)
    name: str
