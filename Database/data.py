import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from Database import main
import string

def search_in_db(ability):
    data = main.get_all_data()
    for x in data:
        list_data = main.mydb[x].find_one({"_id":"Blank"})
        if ability in list_data: return x
    else: return "Called ability not in database"

def find_ability(data="", input=""):
    alpha = list(string.ascii_lowercase)
    characters = []
    for letter in alpha:
        db = main.mydb[data].find_one({"_id":{"$regex": input + letter}})
        if db == None:
            continue
        else: characters.append(db.get("_id"))
    return characters

def find_data(data="", input=""):
    db = main.mydb[data].find_one()
    for x in db:
        if input in x:
            print(x)
        else: continue