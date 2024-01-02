import random

#creating a list of words
word_list = ["apple", "kiwi", "mango", "grapes", "orange"]

#randomly choosing a word from the list using the random module
word = random.choice(word_list)

#asking user for an input
def user_guess():
    guess = input("Please enter a single letter:    ")
    return guess

def check_guess(guess):
    #changes the guess to lower case
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")

def ask_for_input():
    guess = user_guess()
    #validating the input
    while len(guess) != 1 or guess.isalpha() == False:
        print("Oops! That's not a valid input") 
        guess = user_guess()
    
    check_guess(guess)

ask_for_input()
