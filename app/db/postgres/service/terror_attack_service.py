from toolz import partition, partition_all

import app.db.postgres.repository.terror_attack_repository as terror_attack_repos
from app.db.postgres.sql_alchemy_models import TerrorAttack
import app.db.postgres.service.city_service as city_service
import app.db.postgres.service.group_service as group_service
import app.db.postgres.service.attack_type_service as attack_type_service


def terror_attack_data_model_to_terror_attack_sql_model(terror_attack: TerrorAttack, cities_dict: dict, groups_dict: dict, attack_type_dict: dict) -> TerrorAttack:
    return TerrorAttack(
        id=terror_attack.id,
        total_wounded=terror_attack.total_wounded,
        total_killed=terror_attack.total_killed,
        date=terror_attack.date,
        city_id=cities_dict[terror_attack.city.name],
        attack_type_id=attack_type_dict[terror_attack.attack_type.type],
        group_id=groups_dict[terror_attack.group.name]
    )



def create_batches_of_2000_attacks(attacks):
    for attack_batch in partition_all(2000, attacks):
        yield [attack for attack in attack_batch]


def insert_terror_attacks(terror_attacks: list):
    cities_dict = city_service.get_dict_of_key_city_value_city_id()
    groups_dict = group_service.get_dict_of_key_group_value_group_id()
    attack_type_dict = attack_type_service.get_dict_of_key_attack_type_value_attack_type_id()
    parsed_attacks = [terror_attack_data_model_to_terror_attack_sql_model(attack, cities_dict=cities_dict, groups_dict=groups_dict, attack_type_dict=attack_type_dict) for attack in terror_attacks]
    for attacks in create_batches_of_2000_attacks(parsed_attacks):
        terror_attack_repos.insert_terror_attacks(attacks)
        print("inserted a batch")


