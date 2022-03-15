from random import randint
# import random

number = randint(1, 10)
print(number)

guess = int(input('Guess the number (between 1 and 10): '))

while number != guess:
    print('Incorrect...')
    guess = int(input('Try again: '))

print('Correct!')
