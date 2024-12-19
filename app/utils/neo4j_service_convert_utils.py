from typing import List

from app.db.neo4j_db.models import Attack, Country, Group


def unique_countries_from_dict(attacks: List[dict]) -> set:
    return {attack["country"] for attack in attacks}

def unique_groups_from_dict(attacks: List[dict]) -> set:
    return  {attack["group_name"] for attack in attacks}

def dict_to_attack_model(attack: dict) -> Attack:
    return Attack(
        type=attack["attack_type"],
        target=attack["target_type"],
        country=Country(name=attack["country"]),
        group=Group(name=attack["group_name"])
    )

def dicts_to_attack_models(attacks: List[dict]) -> List[Attack]:
    return [dict_to_attack_model(attack) for attack in attacks]
