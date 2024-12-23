from sqlalchemy.orm import relationship

from app.db.postgres.connection import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    country_id = Column(Integer, ForeignKey("country.id"))

    terror_attack = relationship('TerrorAttack', back_populates='city')
    country = relationship('Country', back_populates='city')