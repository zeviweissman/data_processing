from datetime import date
from pydantic import BaseModel
from app.data_models import Group, AttackLocation, TargetType, AttackType


class TerrorAttack(BaseModel):
    date: date
    attack_type: AttackType
    target_type: TargetType
    location: AttackLocation
    group: Group
    total_wounded: int
    total_killed: int
    deadly_score: int
    total_perps: int