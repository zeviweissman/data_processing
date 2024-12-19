from typing import List
from app.db.mongo.connection import get_avg_damage_by_country_collection
from app.db.mongo import crud


def insert_many(data: List[dict]):
    crud.insert_many(data, get_avg_damage_by_country_collection())
