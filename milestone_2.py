import random

#creating a list of words
word_list = ["apple", "kiwi", "mango", "grapes", "orange"]

#randomly choosing a word from the list using the random module
word = random.choice(word_list)

#asking user for an input
def ask_input():
    guess = input("Please enter a single letter:    ")
    return guess

guess = ask_input()

#validating users input
while len(guess) != 1 or guess.isalpha() == False:
    print("Oops! That's not a valid input") 
    guess = ask_input()
else:
    print("Good guess")