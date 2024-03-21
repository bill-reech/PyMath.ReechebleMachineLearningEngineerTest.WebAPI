from pymongo import MongoClient

__all__ = [
    "mongo_client"
]

hostname = 'localhost'
port = 27017

# Create a MongoClient instance
mongo_client = MongoClient(hostname, port)
