#This is Dragon realm the cave choosing game

import random
import time

def show_introduction():
    """This function shows the introduction of the game"""
    
    print('''You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.''')
    
    print()


def chooseCave():
    """This function asks the user to choose a cave and returns it"""
    
    cave = ''

    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave


def checkCave(caveNum):
    """This function will check the cave"""

    print('You approach the cave....')
    time.sleep(2)
    print('It is dark and spooky....')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He open his jaws and....')
    time.sleep(2)

    friendly_cave = random.randint(1,2)

    if caveNum == str(friendly_cave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    show_introduction()
    cave_number = chooseCave()
    checkCave(cave_number)

    print('Do you want to play again? (Yes or No)')
    playAgain = input()
