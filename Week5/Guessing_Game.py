# Week 5 Lab: Guessing Game
# Description: Create a Python program that assigns an integer number (between 0-100) to a variable and prompts the user to guess the number. The program should provide hints if the user's guess is too high or too low (if absolute dierence is > 10), high or low ( if absolute dierence is <=10), and close ( if absolute dierence is <=5) and keep track of the number of attempts made. If the user guesses correctly, it should output amessage announcing the results and number of attempts.

import random

number = random.randint(0, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (between 0 and 100): "))
    attempts += 1
    difference = abs(number - guess)

    if guess == number:
        print(f"Congratulations! You guessed the number {number} correctly in {attempts} attempts.")
        break
    elif difference > 10:
        hint = "too high" if guess > number else "too low"
    elif difference <= 10 and difference > 5:
        hint = "high" if guess > number else "low"
    else:
        hint = "close"
    
    print(f"Your guess is {hint}. Try again!")

