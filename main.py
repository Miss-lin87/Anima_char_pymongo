from Database import main, data
from Characters import Character_functions as CF, main_char as MC
from Functions import Race_functions as Race, Class_functions as Class
import time
import os

character = "None"
suffix = "(New name)"

def menu():
    """This brings up the text of the main menu and then redirects the selection to the actual menu"""
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
    clean()
    if select in options:
        selection(select)
    else: print("Incorrect input, please try again\n\n"); time.sleep(1.5); return menu()

def selection(select=""):
    """This is the actuall menu that will do stuff with the selection"""
    global character
    if select == "1" and character != "None":
        CF.create_char(character.removesuffix(suffix)); clean()
        MC.change_stats(character.removesuffix(suffix)); clean()
        Race.set_race(character.removesuffix(suffix)); clean()
        Class.change_class(character.removesuffix(suffix)); clean()
        print("The character has now been created")
        character = character.removesuffix(suffix); clean()
        return menu()
    elif select == "2": 
        character = input("Select what character to change to: ")
        test = CF.check_char(character)
        if test == False: character = character + suffix; menu()
        else: return menu()
    elif select == "3" and character != "None" and suffix not in character:
        ability = input("What ability is being called? ") 
        print(main.call_one(character.removesuffix(suffix),data.search_in_db(ability), ability))
        return menu()
    elif select == "4" and character != "None" and suffix not in character:
        ability = input("What ability is being changed: ")
        new_value = input("What is the new value of the ability: ")
        main.replace_data(character.removesuffix(suffix),data.search_in_db(ability),ability,new_value)
        return menu()
    elif select == "5": 
        return
    else: error_stuff()

def error_stuff():
    """Will look at and see if the character has a suffix or if the character is None and take action"""
    if suffix in character:
        print("The selected charcater is brand new.\n"
              "Do you want to make a new character of it?", end=" ")
        select = input("Yes or No\n")
        if select in "yes" or "YES":
            return selection(select="1")
        else: return menu()
    elif character == "None":
        print("Please select an active character before anything else \n"
              "Redirecting")
        time.sleep(1)
        return selection(select="2")
    
def clean():
    print("Cleaning consol")
    time.sleep(0.25)
    os.system("cls")
    return

menu()