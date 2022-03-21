from random import randint  # Import the randint function from the random package
# import random

number = randint(1, 10)  # Generate a random number between 1 and 10
print(number)  # Print the number (to make testing easier)

# Ask the user for a guess, and convert the result to an integer
guess = int(input('Guess the number (between 1 and 10): '))

# While the correct number was not guessed...
while number != guess:
    print('Incorrect...')  # Let the user know that their answer was incorrect
    guess = int(input('Try again: '))  # And ask them to guess again

# When the above while loop terminates, that means the correct number was guessed!
print('Correct!')

# Homework: extend the above program so that:
#   1) it generates a number between 1 and 100,
#   2) it gives higher/lower feedback on an incorrect guess.
