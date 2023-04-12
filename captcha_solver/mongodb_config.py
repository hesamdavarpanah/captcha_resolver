import os


class MongoDBConfiguration:
    def __init__(self):
        self.schema = os.getenv("MONGODB_SCHEMA")
        self.username = os.getenv("MONGODB_USERNAME")
        self.password = os.getenv("MONGODB_PASSWORD")
        self.host = os.getenv("MONGODB_HOST")
        self.port = os.getenv("MONGODB_PORT")

    @property
    def mongodb_config(self):
        return f"{self.schema}://{self.username}:{self.password}@{self.host}:{self.port}/"
