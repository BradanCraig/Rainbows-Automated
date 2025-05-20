from pymongo import MongoClient
from bson.objectid import ObjectId
from systems import *
def declare_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Rainbows_DB"]
    return db

def authorize(username, password):
    db = declare_db()
    db = db["users"]
    user = db.find_one({"username": username})

    if user == None:
        return None
    else:
        if user["password"] == password:
            return user
        else:
            print("None")
            return None

def get_user(id) -> dict:
    db = declare_db()
    db = db["users"]
    id_ = ObjectId(id)
    print(id_, type(id_))
    user = db.find_one({"_id": id_})
    print(user)
    return user