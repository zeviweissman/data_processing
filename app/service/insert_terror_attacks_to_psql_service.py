from toolz import pipe
from distributor.distributor import distributor
from app.pandas_.csv_repository import merged_terrorism_dict
import app.utils.psql_service_convert_utils as convert_utils
from app.db.postgres.service import group_service
from app.db.postgres.service import country_service
from app.db.postgres.service import city_service
from app.db.postgres.service import attack_type_service
from app.db.postgres.service import terror_attack_service
from app.db.elastic_db.service import description_service


def insert_groups(groups_to_insert: set):
    group_service.insert_groups(groups_to_insert)


def insert_countries(countries_to_insert: set):
    country_service.insert_countries(countries_to_insert)


def insert_cities(cities_to_insert: set):
    city_service.insert_cities(cities_to_insert)


def insert_attack_types(attacks_types_to_insert: set):
    attack_type_service.insert_attack_types(attacks_types_to_insert)


def insert_terror_attacks(terror_attacks_to_insert: list):
    terror_attack_service.insert_terror_attacks(terror_attacks_to_insert)


def insert_countries_from_cities(cities: set):
    insert_countries(convert_utils.get_unique_countries_from_cities(cities))


def insert_cities_and_countries_from_terror_attacks(terror_attacks: list):
    cities = convert_utils.get_unique_cities_from_terror_attacks(terror_attacks)
    insert_countries_from_cities(cities)
    insert_cities(cities)


def insert_groups_from_terror_attack(terror_attacks: list):
    insert_groups(convert_utils.get_unique_groups_from_terror_attacks(terror_attacks))


def insert_attack_types_from_terror_attacks(terror_attacks: list):
    insert_attack_types(convert_utils.get_unique_attack_types_from_terror_attacks(terror_attacks))


def get_terror_attacks():
    return  pipe(
        merged_terrorism_dict,
        convert_utils.terror_attacks_dicts_to_terror_attacks_models
    )





def insert_data_to_psql():
    distributor(
        get_terror_attacks(),
 insert_cities_and_countries_from_terror_attacks,
        insert_groups_from_terror_attack,
        insert_attack_types_from_terror_attacks,
        insert_terror_attacks,
        description_service.create_descriptions
    )

