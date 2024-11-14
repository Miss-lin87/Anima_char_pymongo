import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from Database import main
from Main_Functions import roll_stats

def get_base_attributes(char=""):
    """This gets all the stats from the Physical Abilities database. All the main stats of the character
    Char is the Character it looks up. Excludes level"""
    attri = main.call_all(char, "Physical_Abilities")
    attri.pop("Level")
    return attri

def change_stats(char=""):
    """This will bring upp the roll stats menu. Then allow the payer to assign the stats to the character in the input.
    Returns a dic of the stats"""
    attri = get_base_attributes(char)
    rolls = roll_stats.menu()
    for stat in attri:
        print(rolls)
        selection = int(input("Please select a value for " + str(stat) + " "))
        main.replace_data(char,"Physical_Abilities", stat, selection)
        rolls.remove(selection)
    return "The stats have been changed. New stats are: \n" + str(get_base_attributes(char))

def change_all_secondary(char=""):
    """This brings up all the secundary stats in order and replaces them with the input.
    Enter is coded to equal 0. This replaces the value not adds to it"""
    attributes = main.call_all(char, "Secondary_Abilities")
    attributes.pop("type")
    for abilility in attributes:
        value = input("What is the new value of " + abilility + ": ")
        if value == "": value = 0
        main.replace_data(char, "Secondary_Abilities", abilility, int(value))
    return

def add_to_secundary(char="", ability=""):
    """This asks for a value and adds it to the ability. Do not replace it but add to it.
    returns nothing"""
    attribute = main.call_one(char, "Secondary_Abilities", ability)
    add = input("How mutch do you want to add to " + ability + " ")
    new_value = attribute + int(add)
    main.replace_data(char, "Secondary_Abilities", ability, new_value)
    return