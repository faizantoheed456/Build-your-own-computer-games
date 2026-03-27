#This is Guess the number game
import random

print("Hello, What's your name?")
name = input()

print(f"Well {name.title()}, I am thinking of a number between 1 and 20.")
number = random.randint(1, 20)

for guess_taken in range(6):

    print('Take a guess')
    guess = input()
    guess = int(guess)

    if guess > number:
        print('Your guess is too high.')
    
    if guess < number:
        print('Your guess is too low.')

    if guess == number:
        break


if guess == number:
    guess_taken = str(guess_taken + 1)
    print(f'Good job, {name.title()}! You guessed my number in {guess_taken} guesses!')

if guess != number:
    number = str(number)
    print(f'Nope! The number I was thinking of was {number}.')