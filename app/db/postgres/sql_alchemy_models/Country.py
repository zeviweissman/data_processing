from sqlalchemy.orm import relationship
from app.db.postgres.connection import Base
from sqlalchemy import Column, Integer, String



class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    city = relationship("City", back_populates='country')