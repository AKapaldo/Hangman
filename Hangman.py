"""
Author: Andrew Kapaldo
Date: October 17, 2020
Version: 1.0
Python 3.8
"""
# Import function
from random import randint

# Variables
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
wordlist = ["MOUSE", "MOOSE", "BUFFALO", "ANTEATER", "GECKO", "CARDINAL", "SHARK", "PENGUIN", "PYTHON", "JAVASCRIPT",
            "RUBY", "FORTRAN", "BASIC", "OATMEAL", "GHOST", "BUCKET", "PAINTING", "FIREWOOD", "TELEVISION"]
turns = 6
guesses = ""
notin = ""
choice = ""


# Functions
def board():
    print(HANGMAN_PICS[len(notin)])
    print("Wrong letters: ", notin)


# Introduce game
print("##################################################")
print("###                  Hangman                   ###")
print("##################################################")
print("\nChoose a letter. Try to complete the word before\nrunning out of turns.\n")
valid = False
while not valid:
    print("What category of words do you want to play?\n 1. Animals\n 2. Programing Languages\n 3. Random")
    gametype = input("Enter your choice: ")
    if gametype == "1":
        choice = randint(0, 8)
        valid = True
    elif gametype == "2":
        choice = randint(8, 12)
        valid = True
    elif gametype == "3":
        choice = randint(0, 18)
        valid = True
    else:
        print("Invalid choice. Pick a number from 1 to 3.\n")
word = wordlist[choice]
while turns > 0:
    wrong = 0
    board()
    for letter in word:
        if letter in guesses:
            print(" ", letter, end="")
        else:
            print(" __", end="")
            wrong += 1
    if wrong == 0:
        print("\nYou Won!")
        break

    guess = input("\nGuess a letter: ").upper()
    guesses += guess
    if guess not in word:
        turns -= 1
        notin += guess
        print(guess, "is not in the word.")
    if turns == 0:
        board()
        print("You lose. Try again.")
    else:
        print("You have", turns, "guesses left.\n")
