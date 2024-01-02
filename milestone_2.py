import random

#creating a list of words
word_list = ["apple", "kiwi", "mango", "grapes", "orange"]

#randomly choosing a word from the list using the random module
word = random.choice(word_list)

#asking user for an input
guess = input("Please enter a single letter:    ")

#validating users input
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess")
else:
    print("Oops! That's not a valid input")