import random

word_list = ["mango", "banana", "blueberry", "blackberry", "grapes"]
print(word_list)
word = random.choice(word_list)
print(word)

def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        check_guess(guess)

def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word {word}")
    elif not guess in word:
        print(f"Sorry, {guess} is not in the word. Try again.")
        ask_for_input()

ask_for_input()
