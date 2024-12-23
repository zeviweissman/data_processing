from typing import List

from toolz import pipe

from app.db.elastic_db.model import DescriptionModel
from app.db.postgres.data_models import TerrorAttackModel


def terror_attack_model_to_description_model(terror_attack: TerrorAttackModel) -> DescriptionModel:
    return DescriptionModel(
        terror_attack_id=terror_attack.id,
        description=",".join(terror_attack.description)
    )

def convert_terror_attacks_to_descriptions(terror_attacks: List[TerrorAttackModel]) -> List[DescriptionModel]:
    return [terror_attack_model_to_description_model(attack) for attack in terror_attacks]

def description_models_to_dicts(descriptions: List[DescriptionModel]) -> List[dict]:
    return [description.model_dump() for description in descriptions]


def convert_terror_attacks_to_description_mapping_with_validation(terror_attacks: List[TerrorAttackModel]) -> List[dict]:
    return pipe(
        terror_attacks,
        convert_terror_attacks_to_descriptions,
        description_models_to_dicts
    )
