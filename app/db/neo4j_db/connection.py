import os
from neo4j import GraphDatabase



NEO4J_URI=os.environ['NEO4J_URI']
NEO4J_USER=os.environ['NEO4J_USER']
NEO4J_PASSWORD=os.environ['NEO4J_PASSWORD']


def get_driver():
    return GraphDatabase.driver(
        NEO4J_URI,
        auth=(NEO4J_USER, NEO4J_PASSWORD)
    )

