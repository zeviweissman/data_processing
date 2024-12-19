import os
from pymongo.mongo_client import MongoClient
from pymongo.synchronous.collection import Collection
from pymongo.synchronous.database import Database


def get_mongo_client() -> MongoClient:
    return MongoClient(os.getenv("MONGO_URI"))


def get_terror_attack_db() -> Database:
    working_environment = os.getenv("ENVIRONMENT", "production")
    if working_environment == 'test':
        return get_mongo_client()['terror_attacks_test']
    else:
        return get_mongo_client()['terror_attacks']


def get_total_damage_by_attack_type_collection() -> Collection:
    return get_terror_attack_db()['damage_by_attack_type']


def get_avg_damage_by_country_collection() -> Collection:
    return get_terror_attack_db()['avg_damage_by_country']


def get_total_damage_by_group_collection() -> Collection:
    return get_terror_attack_db()['total_damage_by_group']


def get_yearly_attack_pct_change_by_country() -> Collection:
    return get_terror_attack_db()['yearly_attack_pct_change_by_country']


def get_active_groups_by_country_collection() -> Collection:
    return get_terror_attack_db()['active_groups_by_country']
