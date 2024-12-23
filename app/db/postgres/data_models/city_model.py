from pydantic import BaseModel, Field
from app.db.postgres.data_models import CountryModel


class CityModel(BaseModel):
    id: int = Field(default=0)
    name: str
    country_id: int = Field(default=0)
    country: CountryModel

    class Config:
        frozen = True


