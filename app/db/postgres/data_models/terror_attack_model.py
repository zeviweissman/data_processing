from datetime import date
from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field, UUID4

from app.db.postgres.data_models import GroupModel, CityModel, AttackTypeModel


class TerrorAttackModel(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    date: date
    attack_type: AttackTypeModel
    attack_type_id: int = Field(default=0)
    city: CityModel
    city_id: int = Field(default=0)
    group: GroupModel
    group_id: int = Field(default=0)
    total_wounded: int
    total_killed: int
    description: List[str]

