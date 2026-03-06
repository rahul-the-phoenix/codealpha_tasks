import random

words = ["python", "apple", "robot", "cloud", "code"]
word = random.choice(words)

guessed = []
tries = 6

print("Welcome to Hangman!")

while tries > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    if display == word:
        print("You won!")
        break

    guess = input("Enter a letter: ")

    if guess in word:
        guessed.append(guess)
    else:
        tries -= 1
        print("Wrong guess! Tries left:", tries)

if tries == 0:
    print("You lost! Word was:", word)