from pydantic import BaseModel, Field


class TargetType(BaseModel):
    id: int = Field(default=0)
    type: str