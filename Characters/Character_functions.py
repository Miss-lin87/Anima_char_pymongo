import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

import pymongo
from Database import main

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["Charactes"]

def get_char():
    """Asks the payer to return the name of the character"""
    char = input("What character do you want to get data from ?")
    return char

def check_char(char="",data="Physical_Abilities"):
    "This checks if a character with the inputed name excsists. Will return true or false"
    test = mydb[data].find_one({"_id":char})
    if test == None:
        return False
    else: return True

def create_char(name="", data=main.get_all_data()):
    """This creates the new Character with the inputed name. 
    Will Copy the Blank ID from the database and change the ID and name to the selected name"""
    for x in data:
        Blank_data = mydb[x].find_one({"_id":"Blank"})
        if x == "Player_information":
            Blank_data["_id"] = name
            Blank_data["Name"] = name
            mydb[x].insert_one(Blank_data)
        else:
            Blank_data["_id"] = name
            mydb[x].insert_one(Blank_data)
    return "character has been created"