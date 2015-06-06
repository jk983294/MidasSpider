from pymongo import MongoClient


def get_mongo_client():
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.prod
    coll = db.stocks
    return client, db, coll
