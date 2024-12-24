from app.db.postgres.data_models import *
from datetime import datetime


def terror_attack_dict_to_terror_attack_model(terror_attack: dict) -> TerrorAttackModel:
    return TerrorAttackModel(
        city=CityModel(
            name=terror_attack['city'],
            country=CountryModel(
                name=terror_attack['country'],
            )
        ),
        attack_type=AttackTypeModel(
            type=terror_attack.get('attack weapon') or terror_attack.get('attack_weapon')
        ),
        group=GroupModel(
          name=terror_attack['perpetrator']
        ),
        total_wounded=terror_attack.get('total wounded') or terror_attack.get('total_wounded'),
        total_killed=terror_attack.get('total killed') or terror_attack.get('total_killed'),
        date=terror_attack['date'] or datetime.now().date(),
        description=[terror_attack['description']]
    )