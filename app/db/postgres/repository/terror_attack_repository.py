from typing import List
from returns.maybe import Maybe, Nothing
from returns.result import Success, Failure
from sqlalchemy.exc import SQLAlchemyError
from app.db.postgres.connection import get_session
from app.db.postgres.sql_alchemy_models import TerrorAttack


def get_all_terror_attacks():
    with (get_session() as session):
        return session.query(TerrorAttack).all()


def insert_terror_attack(terror_attack: TerrorAttack):
    with get_session() as session:
        try:
            session.add(terror_attack)
            session.commit()
            session.refresh(terror_attack)
            return Success(terror_attack)
        except SQLAlchemyError as e:
            print(e)
            return Failure(str(e))


def insert_terror_attacks(terror_attacks :List[TerrorAttack]):
    with get_session() as session:
        try:
            session.add_all(terror_attacks)
            session.commit()
            return Success(True)
        except SQLAlchemyError as e:
            return Failure(str(e))


def get_terror_attack_by_id(terror_attack: int) -> Maybe[TerrorAttack]:
    with get_session() as session:
        return Maybe.from_optional(session.get(TerrorAttack, terror_attack))



def get_terror_attack_by_country(country: str):
    with get_session() as session:
        return Maybe.from_optional(session.query(TerrorAttack).filter(TerrorAttack.city.country.name == country))

def get_terror_attack_by_city(city: str):
    with get_session() as session:
        return Maybe.from_optional(session.query(TerrorAttack).filter(TerrorAttack.city.name == city))

