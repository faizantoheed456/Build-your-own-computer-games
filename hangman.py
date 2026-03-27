import random

HANGMAN_PICS = ['''
                +---+
                    |
                    |
                    |
                   ---''',
                   '''
                +---+
                O   |
                    |
                    |
                   ---''',
                '''
                +---+
                O   |
                |   |
                    |
                   ---''',
                '''
                +---+
                O   |
               /|   |
                    |
                   ---''',
                '''
                +---+
                O   |
               /|\  |
                    |
                   ---''',
                '''
                +---+
                O   |
               /|\  |
               /    |
                   ---''',
                '''
                +---+
                O   |
               /|\  |
               / \  |
                   ---''',
                '''
                +---+
               [O   |
               /|\  |
               / \  |
                   ---''',
                '''
                +---+
               [O]  |
               /|\  |
               / \  |
                   ---''']

words = {
          'fruits': 'apple banana pear strawberry mango'.split(),
          'animals': 'cat dog bear deer lion cow'.split(), 
          'color': 'blue red pink yellow purple'.split(),
          'shapes': 'triangles circle oval rectangle hexagon'.split()
        }

def getRandomWord(wordDict):
    """This function returns a random secret word"""
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord, current_pics):
    """This function displays the blanks and fills them up when user guesses"""
    print(current_pics[len(missedLetters)])
    print()

    print('Missed letters: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print('\n')

def getGuessed(alreadyGuessed):
    """This function returns a single letter from user"""
    while True:
        print('Guess a letter: ')
        guess = input().lower()

        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You\'ve already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a letter.')
        else:
            return guess
        
def playAgain():
    """Restart the game if player wants to play again"""
    print("Do you want to play again? (Yes or No) ")
    return input().lower().startswith('y')

def selectLevel(base_pics):
    """Selects difficulty and returns a modified COPY of the hangman pics"""
    difficulty = 'X'
    while difficulty not in ['E', 'M', 'H']:
        print('Enter difficulty: E-Easy, M-Medium, H-Hard')
        difficulty = input().upper()
        
    game_pics = base_pics.copy() 
    
    if difficulty == 'M':
        del game_pics[8]
        del game_pics[7]
    elif difficulty == 'H':
        del game_pics[8]
        del game_pics[7]
        del game_pics[5]
        del game_pics[3]
        
    return game_pics


print('H A N G M A N')
current_pics = selectLevel(HANGMAN_PICS)
missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print(f'The secret word is in the category: {secretSet.upper()}')
    displayBoard(missedLetters, correctLetters, secretWord, current_pics)
    guess = getGuessed(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess
        
        foundAllTrue = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllTrue = False
                break

        if foundAllTrue:
            print(f'\nYes! The secret word is "{secretWord}"! You have won!')
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(current_pics) - 1:
            displayBoard(missedLetters, correctLetters, secretWord, current_pics)
            print(f'You have run out of guesses!\nAfter {len(missedLetters)} missed '
                  f'guesses and {len(correctLetters)} correct guesses, the word '
                  f'was "{secretWord}"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            current_pics = selectLevel(HANGMAN_PICS)
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False 
            secretWord, secretSet = getRandomWord(words)
            print('\n' * 2)
        else:
            break