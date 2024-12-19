from pydantic import BaseModel

from app.db.neo4j_db.models import Group, Country


class Attack(BaseModel):
    type: str
    target: str
    group: Group
    country: Country