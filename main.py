# Importing modules
from random import randrange
import json

# Variables

dice_1 : int
dice_2 : int
dice_3 : int

def checkThreeOfAKind(d1 : int, d2 : int, d3 : int) -> int:
    """Checks if the 3 values are the same"""

    if d1 == d2 and d2 == d3:
        return 1
    else:
        return 0

def checkFourTwoOnes(d1 : int, d2 :int, d3: int) -> int:
        """Checks if we get 4,2,1"""

        data_list = sorted([d1, d2, d3])
        if data_list == [1, 2, 4]:
            return 1
        else:
             return 0
          

def rollDices(rolls : int) -> dict:
    """This function rolls the 3 dices n amount for times"""
    # setting needed variables
    rolls_data    : dict = {}
    threesOfAKind : int  = 0
    fourTwoOnes   : int  = 0

    # Rolling rolls amount of time
    for roll in range(rolls):
        dice_1 = randrange(1,7)
        dice_2 = randrange(1,7)
        dice_3 = randrange(1,7)

        threesOfAKind    += checkThreeOfAKind(dice_1, dice_2, dice_3)
        fourTwoOnes      += checkFourTwoOnes(dice_1, dice_2, dice_3)

    # putting the data in a dict
    rolls_data = {
        "rolls"        : rolls,
        "threeOfAKind" : threesOfAKind,
        "fourTwoOnes"  : fourTwoOnes
        }


    return rolls_data
    
    

# MAIN

throws : int = int(input("Define the amount of throws..."))

result = rollDices(throws)

print(f"Nombre de lancé: {result['rolls']}\nNombre de Brelan: {result['threeOfAKind']}\nPourcentage de Brelan: {((result['threeOfAKind']) / (result['rolls'])) * 100}%\nNombre de 421: {result["fourTwoOnes"]}\nPourcentage de 421: {((result["fourTwoOnes"]) / (result['rolls'])) * 100} ")

with open('data.json', "w") as f:
    json.dump(result,f)
     
     


    
        

