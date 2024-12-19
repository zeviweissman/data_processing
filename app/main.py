from dotenv import load_dotenv
load_dotenv(verbose=True)

from app.service.insert_stats_to_mongo_service import insert_all_stats_to_mongo


if __name__ == '__main__':
    insert_all_stats_to_mongo()