from pydantic import BaseModel, Field

class AttackType(BaseModel):
    id: int = Field(default=0)
    type: str