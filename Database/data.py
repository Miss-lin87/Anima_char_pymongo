import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from Database import main
import string

def search_in_db(ability):
    """This will seartch the entire database and find the sub database the ability is in.
    For instance Player_information for things like name, movement and experiance"""
    data = main.get_all_data()
    for x in data:
        list_data = main.mydb[x].find_one({"_id":"Blank"})
        if ability in list_data: return x
    else: return "Called ability not in database"

def find_character(data="Player_information", input=""):
    """This will seartch the database for all ID tags and return there names.
    A way to get all the names of characters in the database. DO NOT change data"""
    alpha = list(string.ascii_lowercase)
    characters = []
    for letter in alpha:
        db = main.mydb[data].find_one({"_id":{"$regex": input + letter}})
        if db == None:
            continue
        else: characters.append(db.get("_id"))
    return characters

def find_data(data="", input=""):
    """Seartches the database for the input, well return all instances that contain the input.
    Data is the dabase to be seartched"""
    db = main.mydb[data].find_one()
    print(db)
    for x in db:
        if input in x:
            print(x)
        else: continue