from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from db.appConfigs import settings


class MongoDatabaseConnector:
    """Singleton class to connect to MongoDB database."""

    _instance: MongoClient = None

    def __new__(cls):
        if cls._instance is None:
            try:
                cls._instance = MongoClient(settings.MONGO_DATABASE_HOST)
            except ConnectionFailure as e:
                print(f"Couldn't connect to the database: {str(e)}")
                raise

        return cls._instance
    
    def close(self):
        if self._instance:
            self._instance.close()



mongo_connection = MongoDatabaseConnector()