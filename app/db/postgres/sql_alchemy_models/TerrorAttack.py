from sqlalchemy.orm import relationship
from app.db.postgres.connection import Base
from sqlalchemy import Column, Integer, String, DATE, ForeignKey


class TerrorAttack(Base):
    __tablename__ = 'terror_attack'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DATE)
    attack_type_id = Column(Integer, ForeignKey('attack_type.id'))
    city_id = Column(Integer, ForeignKey('city.id'))
    group_id = Column(Integer, ForeignKey('group.id'))
    total_wounded = Column(Integer)
    total_killed = Column(Integer)


    attack_type = relationship('AttackType', back_populates='terror_attack')
    city = relationship('City', back_populates='terror_attack')
    group = relationship('Group', back_populates='terror_attack')
