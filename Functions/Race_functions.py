import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from Database import main

humans = ["Asher", "Aion", "Tayahar", "Zinner", "Ryuan", "Norne", "Vildian", "Daevar", "Kwa", "Celsus"]
nephilim = ["Sylvian", "Jayan", "DAnjayni", "Ebudan", "Daimah", "Dukzarist"]

def set_race(char=""):
    print("Human race: " + str(humans))
    print("Nephilim races: " + str(nephilim))
    selection = input("Please select a race to play: ")
    if selection in humans:
        main.replace_data(char,"Player_information", "Race", selection)
        return "race has been set"
    elif selection in nephilim:
        main.replace_data(char,"Player_information", "Race", selection)
        return "race has been set"
    else: print("Not a valid option"); return set_race(char)