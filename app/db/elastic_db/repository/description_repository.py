from typing import List

from elasticsearch import helpers

from app.db.elastic_db.connection import get_elastic_client
import os


DESCRIPTION_INDEX = os.environ['DESCRIPTION_INDEX']

def create_descriptions(descriptions: List[dict]):
    try:
        helpers.bulk(
            client=get_elastic_client(),
            actions=descriptions,
            chunk_size=1000,
            index=DESCRIPTION_INDEX)
    except Exception as e:
        print(e)