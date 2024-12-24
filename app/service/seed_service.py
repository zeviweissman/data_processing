from app.service.insert_terror_attacks_to_psql_service import insert_data_to_psql_and_elastic
from app.service.insert_relations_to_neo4j_service import insert_all_relations_to_neo4j
from app.service.insert_stats_to_mongo_service import insert_all_stats_to_mongo



def seed_data():
    insert_all_stats_to_mongo()
    print("inserted all stats to mongo")
    # insert_all_relations_to_neo4j()
    # print("inserted all relations to neo4j")
    insert_data_to_psql_and_elastic()
    print("inserted data to psql")