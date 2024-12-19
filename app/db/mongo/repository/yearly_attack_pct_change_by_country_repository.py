from typing import List
from app.db.mongo.connection import get_yearly_attack_pct_change_by_country
from app.db.mongo import crud


def insert_many(data: List[dict]):
    crud.insert_many(data, get_yearly_attack_pct_change_by_country())
