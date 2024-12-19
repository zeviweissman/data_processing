from typing import List
from pymongo.synchronous.collection import Collection


def insert_many(data: List[dict], collection:Collection):
        collection.insert_many(data)
