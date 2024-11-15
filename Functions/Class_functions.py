import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from Database import main

classes = ["Tao", "Technician", "Acrobatic Warrior", "Dark Paladin",
"Paladin", "Ranger", "Shadow", "Tao", "Warlock", "Warrior", "Warrior Mentalist"
"Warrior Summoner", "Weaponmaster"]

def change_class(char=""):
    print(classes)
    selection = input("Please select a class from the list: ")
    if selection in classes: 
        main.replace_data(char, "Player_information", "Class", selection)
        return "Class hans been set"
    else: print("Not a valid input, try again\n"); return change_class(char)