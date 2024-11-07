from dice import D10
import time

def menu():
    """This calles the menu for rolling stats. One call instead of nested"""
    rolls = selection(menu_text())
    return rolls

def menu_text():
    """This brings up the text of the menu and gives you choses to pick. the selection is made with just numbers"""
    print("Please make a selection:\n"
          "1. Method one\n"
          "2. Method two\n"
          "3. Method three\n"
          "4. Explain the methods\n"
          "5. Exit\n")
    slect = input("Make a selection ")
    return str(slect)
    
def selection(slect):
    """This function only works in tandom with the menu function. This one calls the specific functions based on choice"""
    if slect == "1": time.sleep(0.25); return method_one()
    elif slect == "2": time.sleep(0.25); return method_two()
    elif slect == "3": time.sleep(0.25); return method_thre()
    elif slect == "4": time.sleep(0.25); explain(); return menu()
    elif slect == "5": time.sleep(0.25); return
    else: print("Wrong selection made. Please try again "); time.sleep(0.25); return selection()

def explain():
    """This function explains the different rolls and what they mean"""
    print("Method one:\n"
          "The computer rolls 1d10 8 times rerolling 1,2 and 3\n"
          "After this the lowest roll is replaced with a 10\n"
          "Method two:\n"
          "This rolls 2d10 8 times and keeps the higher of the two rolls every time\n"
          "Method three:\n"
          "This just rolls 1d10 8 times and keeps the result every time.\n")
    input("Press any key to continue...")

# This is the first method of rolling stats. It Rolls stats 8 times, rerolling 1,2 and 3.
# Then replaces the lowest number rolled with a 10.
def method_one():
    """This is the first metod of rolling stats. Were the lowest number is replaced with a 10 and 1-3 is ignored"""
    rolls = []
    x = 8
    while x > 0:
        roll = D10()
        if roll in range(4,10): x -= 1; rolls.append(roll); remove_low(rolls)
        else: continue
    else: return rolls

def remove_low(rolls):
    """This function will sort the list. The pop the lowest value and add a 10"""
    sortR = sorted(rolls)
    sortR.pop(0)
    sortR.append(10)
    return sortR
# end of the functions to roll metod one

# This is the start of method two for rolling stats. 
# You roll 2d10 and take the highest roll. This is done 8 times
def method_two():
    """This method rolls 2d10 and keeps the higher of the two. Adds them to a list and returns the list"""
    rolls = []
    x = 8
    while x > 0:
        roll1 = D10()
        roll2 = D10()
        if roll1 > roll2: x -=1; rolls.append(roll1)
        else: x-= 1; rolls.append(roll2)
    return rolls
# This is the end of the secound method for rolling stats

# Begining of method 3 for rolling stats.
# This is the simplest method. Just roll 1d10 8 times and add it to a list
def method_thre():
    """This function rolls stats with just 1d10 8 times"""
    rolls = []
    x = 8
    while x > 0:
        roll = D10()
        rolls.append(roll)
        x -= 1
    return rolls
# This marks the end of the therd way to roll stats.