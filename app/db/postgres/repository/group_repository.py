from returns.maybe import Maybe
from returns.result import Success, Failure, Result
from sqlalchemy.exc import SQLAlchemyError
from app.db.postgres.connection import get_session
from app.db.postgres.sql_alchemy_models import Group


def get_groups():
    with get_session() as session:
        return session.query(Group).all()


def get_group_by_name(group_name: str) -> Maybe[Group]:
    with get_session() as session:
        return Maybe.from_optional(
            session.query(Group).filter(Group.name == group_name).first()
        )


def insert_group(group:Group):
    with get_session() as session:
        try:
            session.add(group)
            session.commit()
            session.refresh(group)
            return Success(group)
        except SQLAlchemyError as e:
            return Failure(str(e))


def getsert_groups(group_name: str) -> Result[Group, str]:
    if group_exists := get_group_by_name(group_name).value_or(None):
        return Success(group_exists)
    return insert_group(Group(name=group_name))