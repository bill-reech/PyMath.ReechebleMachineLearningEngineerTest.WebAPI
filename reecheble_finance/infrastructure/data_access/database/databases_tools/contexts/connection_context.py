from typing import Callable

from pymongo import MongoClient

from reecheble_finance.infrastructure.data_access.database.databases_tools.connections.connections import mongo_client

__all__ = [
    "mongo_database_context"
]

mongo_database_context: Callable[[], MongoClient] = lambda: mongo_client
