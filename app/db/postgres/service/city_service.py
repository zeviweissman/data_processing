import app.db.postgres.repository.city_repository as city_repository
from app.db.postgres.sql_alchemy_models import City
from app.db.postgres.data_models import CityModel
import app.db.postgres.service.country_service as country_service


def city_data_model_to_city_sql_model(city: str, countries_dict: dict) -> City:
    return City(
        name=city.name,
        country_id=countries_dict[city.country.name],
    )



def insert_cities(cities: set):
    countries_dict = country_service.get_dict_of_key_country_value_country_id()
    for city in cities:
        city_repository.getsert_city(city_data_model_to_city_sql_model(city, countries_dict))


def get_dict_of_key_city_value_city_id():
    return {city.name : city.id for city in city_repository.get_cities()}


