from typing import Callable

from pymongo import MongoClient


__all__ = [
    "mongo_database_context"
]


mongo_database_context: Callable[[], MongoClient] = lambda: MongoClient('mongodb://localhost:27017/')
