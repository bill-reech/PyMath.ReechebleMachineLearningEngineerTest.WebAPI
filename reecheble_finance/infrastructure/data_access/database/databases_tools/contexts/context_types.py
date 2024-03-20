from pymongo import MongoClient

from reecheble_finance.infrastructure.data_access.context import ServiceContext
from reecheble_finance.infrastructure.data_access.database.databases_tools.contexts.connection_context import (
    mongo_database_context)

__all__ = [
    "PyMongoDbContext"
]


class PyMongoDbContext(ServiceContext):
    session: MongoClient = None

    def __init__(self) -> None:
        self.mongo_session: MongoClient = self.__class__.session or self.get_database_context()
        super().__init__(context=self.mongo_session)

    def close(self) -> None:
        self.context.close()

    def commit(self) -> None:
        self.context.commit()

    def rollback(self) -> None:
        self.context.rollback()

    @staticmethod
    def get_database_context():
        return mongo_database_context()
