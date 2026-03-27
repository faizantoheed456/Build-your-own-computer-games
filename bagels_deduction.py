import random

MAX_DIGITS = 3
MAX_GUESS = 10

def getSecretNumber():
    """Generates a 3 digits secret number with only unique digits"""

    numbers = list(range(10))
    random.shuffle(numbers)

    secret_Num = ''
    
    for i in range(MAX_DIGITS):
        secret_Num += str(numbers[i])
    return secret_Num


def getClues(guess, secretNum):
    """Returns a string with the Pico, Fermi and bagels clues to the user"""

    if guess == secretNum:
        return 'You got it'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    
    clues.sort()
    return ' '.join(clues)


def isOnlyDigits(num):
    """Returns True if the number is a string of only digits. Otherwise, returns False"""

    if num == ' ':
        return False
    
    return num.isdigit()



print(f'I am thinking of a {MAX_DIGITS}-digits number. Try to guess it!')
print('The clues I gave are...')
print('When I say:      That means:')
print('    Bagles:      None of the digits is correct.')
print('      Pico:      One digit is correct but in the wrong position.')
print('     Fermi:      One digit is correct but in the right position.')

while True:

    secretNum = getSecretNumber()
    print(f'I have thought up a number. You\'ve {MAX_GUESS}-guesses to get it.')

    guesses_taken = 1
    while guesses_taken <= MAX_GUESS:
        guess = ''
        while len(guess) != MAX_DIGITS or not isOnlyDigits(guess):
            print(f'Guess #{guesses_taken}: ')
            guess = input()

        print(getClues(guess, secretNum))
        guesses_taken += 1

        if guess == secretNum:
            break
        if guesses_taken > MAX_GUESS:
            print(f'You are ran out of guesses. The answer was {secretNum}.')

    print('Do you want to play again? (Yes or no)')
    if not input().lower().startswith('y'):
        break