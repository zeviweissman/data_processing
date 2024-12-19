from dotenv import load_dotenv
load_dotenv(verbose=True)

from app.db.mongo.connection import get_mongo_client
from app.db.neo4j_db.connection import get_driver
from app.service.insert_relations_to_neo4j_service import insert_all_relations_to_neo4j
from app.service.insert_stats_to_mongo_service import insert_all_stats_to_mongo


if __name__ == '__main__':
    get_mongo_client().drop_database('terror_attacks')
    insert_all_stats_to_mongo()
    get_driver().session().run(query="MATCH (n) detach delete n")
    insert_all_relations_to_neo4j()