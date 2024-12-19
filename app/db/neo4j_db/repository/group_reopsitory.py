from app.db.neo4j_db.crud import create


def recreate_group(group: str):
    return create({"name": group}, ["Group"])
