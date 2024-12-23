from app.pandas_.csv_repository import merged_terrorism_dict
import app.utils.psql_service_convert_utils as convert_utils
from app.db.postgres.service import group_service
from app.db.postgres.service import country_service
from app.db.postgres.service import city_service
from app.db.postgres.service import attack_type_service
from app.db.postgres.service import terror_attack_service






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

def insert_attacks_to_psql():
    raw_data = merged_terrorism_dict
    attacks = convert_utils.terror_attacks_dicts_to_terror_attacks_models(raw_data)
    cities = convert_utils.get_unique_cities_from_terror_attacks(attacks)
    countries = convert_utils.get_unique_countries_from_cities(cities)
    attack_types = convert_utils.get_unique_attack_types_from_terror_attacks(attacks)
    groups = convert_utils.get_unique_groups_from_terror_attacks(attacks)
    insert_countries(countries)
    insert_cities(cities)
    insert_groups(groups)
    insert_attack_types(attack_types)
    insert_terror_attacks(attacks)