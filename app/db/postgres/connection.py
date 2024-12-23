import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy_repr import RepresentableBase
from sqlalchemy_utils import database_exists, drop_database, create_database


PSQL_URL = os.getenv('PSQL_URL')

Base = declarative_base()
#Base = declarative_base(cls=RepresentableBase)
engine = create_engine(url=PSQL_URL)
_session_factory = sessionmaker(bind=engine)


def get_session():
    return _session_factory()


def drop_database_if_exists():
    if database_exists(PSQL_URL):
        drop_database(PSQL_URL)


def create_database_if_not_exists():
    if not database_exists(PSQL_URL):
        create_database(PSQL_URL)


def create_tables_if_not_exists():
    Base.metadata.create_all(engine)


def drop_tables_if_exists():
    Base.metadata.drop_all(engine)

def init_db():
    create_database_if_not_exists()
    create_tables_if_not_exists()


