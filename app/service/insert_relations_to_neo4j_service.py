from app.pandas_.csv_repository import extended_global_terrorism_dict
import app.utils.neo4j_service_convert_utils as convert_utils
import app.db.neo4j_db.repository.country_repository as country_repository
import app.db.neo4j_db.repository.group_reopsitory as group_repository
import app.db.neo4j_db.repository.attack_repository as attack_repository


raw_data_dict = extended_global_terrorism_dict



def insert_countries():
    countries = convert_utils.unique_countries_from_dict(raw_data_dict)
    for country in countries:
        country_repository.create_country(country)

def insert_groups():
    groups = convert_utils.unique_groups_from_dict(raw_data_dict)
    for group in groups:
        group_repository.recreate_group(group)

def insert_attacks():
    attacks = convert_utils.dicts_to_attack_models(raw_data_dict)
    for attack in attacks:
        attack_repository.create_attack(attack)


def insert_all_relations_to_neo4j():
    insert_countries()
    insert_groups()
    insert_attacks()