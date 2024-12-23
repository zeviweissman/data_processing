from returns.maybe import Maybe
from returns.result import Success, Failure, Result
from sqlalchemy.exc import SQLAlchemyError
from app.db.postgres.connection import get_session
from app.db.postgres.sql_alchemy_models import AttackType


def get_attack_types():
    with get_session() as session:
        return session.query(AttackType).all()


def get_attack_types_by_name(attack_type: str) -> Maybe[AttackType]:
    with get_session() as session:
        return Maybe.from_optional(
            session.query(AttackType).filter(AttackType.name == attack_type).first()
        )


def insert_attack_type(attack: AttackType):
    with get_session() as session:
        try:
            session.add(attack)
            session.commit()
            session.refresh(attack)
            return Success(attack)
        except SQLAlchemyError as e:
            return Failure(str(e))


def getsert_attack_type(attack_type: str) -> Result[AttackType, str]:
    if attack_type_exists := get_attack_types_by_name(attack_type).value_or(None):
        return Success(attack_type_exists)
    return insert_attack_type(AttackType(name=attack_type))