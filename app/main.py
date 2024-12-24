from dotenv import load_dotenv
load_dotenv(verbose=True)


from app.db.postgres.sql_alchemy_models import *
from app.service.seed_service import seed_data
from app.service.subscribe_terror_attacks_news import consume_terror_attacks


if __name__ == '__main__':
    seed_data()
    consume_terror_attacks()