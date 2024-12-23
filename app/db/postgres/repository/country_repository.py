from returns.maybe import Maybe
from returns.result import Success, Failure, Result
from sqlalchemy.exc import SQLAlchemyError
from app.db.postgres.connection import get_session
from app.db.postgres.sql_alchemy_models import Country


def get_countries():
    with get_session() as session:
        return session.query(Country).all()


def get_country_by_name(country_name: str) -> Maybe[Country]:
    with get_session() as session:
        return Maybe.from_optional(
            session.query(Country).filter(Country.name == country_name).first()
        )


def insert_country(country:Country):
    with get_session() as session:
        try:
            session.add(country)
            session.commit()
            session.refresh(country)
            return Success(country)
        except SQLAlchemyError as e:
            return Failure(str(e))


def getsert_country(country_name: str) -> Result[Country, str]:
    if country_exists := get_country_by_name(country_name).value_or(None):
        return Success(country_exists)
    return insert_country(Country(name=country_name))