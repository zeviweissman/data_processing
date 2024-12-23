from pydantic import BaseModel, Field


class CountryModel(BaseModel):
    id: int = Field(default=0)
    name: str
    class Config:
        frozen = True