from pydantic import BaseModel, Field


class AttackLocation(BaseModel):
    id: int = Field(default=0)
    country: str
    region: str
    province_or_state: str
    city: str
    lat: float
    lon: float
