from pydantic import BaseModel, Field

class Group(BaseModel):
    id: int = Field(default=0)
    name: str
