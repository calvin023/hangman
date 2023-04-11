import csv
import os
import random

# Setting up variables
wrong_guess = []
cor_letters = []
cor_guess = []
amount_of_guesses = 0
hangman = ""

# Selecting a random word
current_dir = os.path.dirname(os.path.abspath(__file__))
filename = 'words.csv'
with open(os.path.join(current_dir, filename), newline='') as csvfile:
    reader = csv.reader(csvfile)
    wordlist = list(reader)
# Choose word from random index
word = random.choice(wordlist)[0]
# Filling the correct letters list
for c in word:
    cor_letters.append(c)

# Filling in correct guesses list
for c in word:
    cor_guess.append("_")

print(' '.join(cor_guess))

while cor_guess != cor_letters:
    if amount_of_guesses == 0:
        pass
    elif amount_of_guesses == 1:
        hangman = "  O"
    elif amount_of_guesses == 2:
        hangman = "  O\n  |\n  |"
    elif amount_of_guesses == 3:
        hangman = "  O\n /|\n/ |"
    elif amount_of_guesses == 4:
        hangman = "  O\n /|\\\n/ | \\"
    elif amount_of_guesses == 5:
        hangman = "  O\n /|\\\n/ | \\\n /\n/"
    if amount_of_guesses < 6:
        print(hangman)
        if wrong_guess != []:
            print("Wrong guesses: ", ", ".join(wrong_guess))
        letter = input("Guess a letter: ")
        letter = letter.lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single alphabetic letter.")
        elif letter in cor_letters:
            for i in range(len(word)):
                if word[i] == letter:
                    cor_guess[i] = letter
            print(" ".join(cor_guess))
        elif letter not in cor_letters and letter not in wrong_guess:
            print(letter, "is incorrect")
            wrong_guess.append(letter)
            amount_of_guesses += 1
    else:
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        hangman = "  O\n /|\\\n/ | \\\n / \\\n/   \\"
        print("You lose")
        print(hangman)
        print("The word was: %s" % word)
        break
        
if cor_guess == cor_letters:
    print("You've guessed the word, it was: %s" % word)
else:
    pass
