from returns.maybe import Maybe
from returns.result import Success, Failure, Result
from sqlalchemy.exc import SQLAlchemyError
from app.db.postgres.connection import get_session
from app.db.postgres.sql_alchemy_models import City


def get_cities():
    with get_session() as session:
        return session.query(City).all()


def get_city_by_name(city_name: str) -> Maybe[City]:
    with get_session() as session:
        return Maybe.from_optional(
            session.query(City).filter(City.name == city_name).first()
        )


def insert_city(city:City):
    with get_session() as session:
        try:
            session.add(city)
            session.commit()
            session.refresh(city)
            return Success(city)
        except SQLAlchemyError as e:
            return Failure(str(e))


def getsert_city(city: City) -> Result[City, str]:
    if city_exists := get_city_by_name(city.name).value_or(None):
        return Success(city_exists)
    return insert_city(city)