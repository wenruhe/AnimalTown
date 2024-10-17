from neo4j import GraphDatabase, RoutingControl
from db.configs import settings

class Neo4jConnector:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            try:
                cls._instance = GraphDatabase.driver(settings.NEO4J_URI, auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD))
                cls._instance.verify_connectivity()
            except Exception as e:
                print(e)
                raise
        return cls._instance

    def close(self):
        if self._instance:
            self._instance.close()
        

neo4jConnector = Neo4jConnector()