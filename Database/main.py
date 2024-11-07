import pymongo

Raw_data = {}

def set_up_DB():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Anima"]
    mycol = mydb["Characters"]