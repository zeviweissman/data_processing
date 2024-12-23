import app.db.postgres.repository.country_repository as country_repository


def insert_countries(countries: set):
    for country in countries:
        country_repository.getsert_country(country)


def get_dict_of_key_country_value_country_id():
    return {country.name : country.id for country in country_repository.get_countries()}