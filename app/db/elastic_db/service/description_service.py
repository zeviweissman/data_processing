from typing import List
import app.db.elastic_db.repository.description_repository as description_repository
from app.db.postgres.data_models import TerrorAttackModel
import app.utils.elastic_convert_utils as convert_utils


def create_descriptions(terror_attacks: List[TerrorAttackModel]):
    description_repository.create_descriptions(convert_utils.convert_terror_attacks_to_description_mapping_with_validation(terror_attacks))
