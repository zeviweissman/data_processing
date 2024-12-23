from pydantic import BaseModel, Field

class AttackTypeModel(BaseModel):
    id: int = Field(default=0)
    type: str