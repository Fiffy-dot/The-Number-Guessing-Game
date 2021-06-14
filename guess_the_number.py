from art import logo
import random

# print logo
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100....")
# user picks difficulty level
level = input("Pick a difficulty playing level. Type 'easy' for beginner or 'hard' for advanced: ")

lives = 0
if level == "easy":
    lives = 10
elif level == "hard":
    lives = 5

# pick a random number for the user to guess
picked_number = random.choice(range(1, 101))
while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess == picked_number:
        print(f"You won, the number was {picked_number}")
        quit()
    else:
        lives -= 1
        if guess > picked_number:
            print("Too high")
            print("Guess again")
        else:
            print("Too low")
            print("Guess again")

if lives == 0:
    print("Sorry you ran out of lives, you lose")
