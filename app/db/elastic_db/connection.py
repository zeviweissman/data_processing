from elasticsearch import Elasticsearch
import os




DESCRIPTION_INDEX = os.environ['DESCRIPTION_INDEX']


def get_elastic_client():
    return Elasticsearch(
        ['http://localhost:9200']
    )


def setup_description_index():
    with get_elastic_client() as elastic_client:
        if not elastic_client.indices.exists(index=DESCRIPTION_INDEX):
            elastic_client.indices.create(index=DESCRIPTION_INDEX, body={
                "mappings": {
                    "properties": {
                        "terror_attack_id": {"type": "text"},
                        "description": {"type": "text"},
                }
            }
       }
    )


def drop_description_index():
    with get_elastic_client() as elastic_client:
        if elastic_client.indices.exists(index=DESCRIPTION_INDEX):
            elastic_client.indices.delete(index=DESCRIPTION_INDEX)

