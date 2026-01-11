# Guess the Number Game

import random

number = random.randint(1, 100)
attempts = 0

print("Welcome to Guess the Number Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it.\n")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try a higher number.\n")
    elif guess > number:
        print("Too high! Try a lower number.\n")
    else:
        print("Congratulations! You guessed the correct number.")
        print("Total attempts:", attempts)
        break
