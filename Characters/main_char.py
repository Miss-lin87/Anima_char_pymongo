import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from Database import main
from Main_Functions import roll_stats

def get_base_attributes(char=""):
    attri = main.call_all(char, "Physical_Abilities")
    attri.pop("Level")
    return attri

def change_stats(char=""):
    attri = get_base_attributes(char)
    rolls = roll_stats.menu()
    for stat in attri:
        print(rolls)
        selection = int(input("Please select a value for " + str(stat) + " "))
        main.replace_data(char,"Physical_Abilities", stat, selection)
        rolls.remove(selection)
    return "The stats have been changed. New stats are: \n" + str(get_base_attributes(char))