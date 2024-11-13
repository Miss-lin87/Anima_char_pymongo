from Main_Functions import roll_stats
from Database import main, data
from Characters import Character_functions as CF
from Calulations import main_calc
import time

character = "None"

def menu():
    global character
    print("Main menu.\n"
          "The selected character is: " + character + "\n"
          "1. Make a new character\n"
          "2. Change the selected character\n"
          "3. Print the stats of a selected character\n"
          "4. Change the stats of a character\n"
          "5. Exit")
    options = ["1","2","3","4","5"]
    select = input("Please make a selection: ")
    if select in options:
        selection(select)
    else: print("Incorrect input, please try again\n\n"); time.sleep(1.5); return menu()

def selection(select=""):
    global character
    if select == "1": CF.create_char(character); return menu()
    elif select == "2": 
        character = input("Select what character to change to: ")
        test = CF.check_char(character)
        if test == False: character = character + "(New name)"; menu()
        else: return menu()
    elif select == "3":
        ability = input("What ability is being called? ") 
        print(main.call_one(character,data.search_in_db(ability), ability)); return menu()
    elif select == "4": main.replace_data(character,"Physical_Abilities","Agility",5); return menu()
    elif select == "5": return

print(menu())
