from pymongo import MongoClient, errors


class Logger:
    def __init__(self, mongodb_config):
        self.mongodb_config = mongodb_config
        self.client = MongoClient(self.mongodb_config)
        self.database = None
        self.collection = None

    def mongodb_database(self, dbname):
        try:
            database = self.client[dbname]
            return database
        except errors.PyMongoError as error:
            return error

    def mongodb_collection(self, database, coll_name):
        try:
            collection = database[coll_name]
            return collection
        except errors.CollectionInvalid as error:
            return error

    def mongodb_insert_one(self, collection, data):
        try:
            out = collection.insert_one(data)
            return out
        except errors.InvalidDocument as error:
            return error
