from sqlalchemy.orm import relationship

from app.db.postgres.connection import Base
from sqlalchemy import Column, Integer, String


class AttackType(Base):
    __tablename__ = 'attack_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    terror_attack = relationship('TerrorAttack', back_populates='attack_type')
