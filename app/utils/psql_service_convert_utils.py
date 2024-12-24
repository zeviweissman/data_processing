from typing import  List, Set
from app.db.postgres.data_models import TerrorAttackModel, CityModel, CountryModel, AttackTypeModel, GroupModel




def terror_attack_dict_to_terror_attack_model(terror_attack: dict) -> TerrorAttackModel:
    return TerrorAttackModel(
        city=CityModel(
            name=terror_attack['city'],
            country=CountryModel(
                name=terror_attack['country'],
            )
        ),
        attack_type=AttackTypeModel(
            type=", ".join(terror_attack['attack_type'])
        ),
        group=GroupModel(
          name=terror_attack['group_name']
        ),
        total_wounded=int(terror_attack['total_wounded']),
        total_killed=terror_attack['total_killed'],
        date=terror_attack['date'],
        description=terror_attack['description']
    )


def terror_attacks_dicts_to_terror_attacks_models(terror_attacks: List[dict]) -> List[TerrorAttackModel]:
    return [terror_attack_dict_to_terror_attack_model(terror_attack) for terror_attack in terror_attacks]


def get_unique_cities_from_terror_attacks(attacks: List[TerrorAttackModel]) -> Set[CityModel]:
    return {attack.city for attack in attacks}

def get_unique_countries_from_cities(cities: Set[CityModel]) -> Set[str]:
    return {city.country.name for city in cities}

def get_unique_groups_from_terror_attacks(attacks: List[TerrorAttackModel]) -> Set[str]:
    return {attack.group.name for attack in attacks}

def get_unique_attack_types_from_terror_attacks(attacks: List[TerrorAttackModel]) -> Set[str]:
    return {attack.attack_type.type for attack in attacks}
