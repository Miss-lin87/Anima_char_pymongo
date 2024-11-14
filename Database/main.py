import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["Charactes"]

def call_all(char="", data=""):
    """This is used to call all the data from a section of the database. Will drop the _id on call"""
    data = mydb[data].find_one({"_id":char})
    data.pop("_id")
    return data

def call_one(char="", data="", abillity=""):
    """This will call one specific abiloty from the data section of the database. will only return value"""
    data = mydb[data].find_one({"_id":char})
    return data[abillity]

def replace_data(char="", data="", abillity="", new_data=""):
    """This will replace the called abillity from the data section of the database with the new_data value"""
    query = {"_id":char}
    temp_query = mydb[data].find_one(query)
    temp_query[abillity] = new_data
    mydb[data].update_many(query, {"$set":temp_query})
    return

def get_all_data():
    """This will get the name of all the diffrent sub databases like Player_information, and Physical_Abilities """
    mydb = client["Charactes"]
    return mydb.list_collection_names()