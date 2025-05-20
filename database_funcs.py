from pymongo import MongoClient

def declare_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Rainbows_DB"]
    return db

def authenticate(username, password):
    db = declare_db()
    db = db["users"]
    print("searching")
    user = db.find_one({"username": username})
    print(user)

authenticate("test","test")
