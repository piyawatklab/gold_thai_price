import pymongo
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://admin:1234@mern-workshop.4w7y5.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]


def all():
    response = collection.find({})
    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data

def get_one(condition):
    response = collection.find({"date": condition}).sort("cnt",-1)
    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)

    if len(data) >> 0 :
        return data[0]
    else :
        return get_last()

def get_by_date(date):
    response = collection.find({"date": date}).sort("cnt",-1)
    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data

def get_last():
    response = collection.find({}).sort([("date",-1), ("cnt",-1)])

    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data[0]
