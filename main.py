# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


import random


def rolling():
  a="        \"The Roling the dice game...\""
  print(a.upper(),"\n==================================================\n\n\n\n")
  b="Welcome to the roling the dice game...\n\n\n\n"
  print(b.capitalize())
  # sleep for 2 seconds after printing output
  sleep(3)
  clear()
def heading():
  a="        \"The Roling the dice game\""
  print(a.upper(),"\n==================================================\n\n\n\n")
def userInput():
  userInput=input("Enter The Number You Guessed...\n(1 / 2 / 3 / 4 / 5 / 6 )\n\n---> ")
  print ("\n\nRolling the dices...")
def userInpProg(): 
  heading()
  userInput()
  clear()
def itsRolling():
  heading()
  print ("\nRolling the dice....")
  sleep(3)
  clear()
def processing(): 
  min = 1
  max = 6
  dieResult=random.randint(min, max)
  roll_again = "yes"

  while roll_again == "yes" or roll_again == "y":
    clear()
    userInpProg()
    itsRolling()
    heading()
    checking()
    roll_again = input("Want to roll the dices again?\n( Y / N )\n--->")

rolling()
processing()