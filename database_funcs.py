from pymongo import MongoClient

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

