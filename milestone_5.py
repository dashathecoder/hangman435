import random

class Hangman:

    """
    This class represents the Hangman game.
    
    Args:
        word_list(list): the list of words for the game, one of which is randomly chosen as the hangman word.
        num_lives(int): the number of lives the user has to guess the word.
        
    Initialised variables:
        word(str): the word chosen from the list of words.
        word_guessed(list): a list of underscores the length of the word, which get replaced with the letters as they are guessed.
        num_letters(int): the number of letters in the chosen word.
        list_of_guesses(list): a list of the letters guessed by user. 
    """
    def __init__(self, word_list, num_lives = 5):
        #chosing the word
        word_list = word_list
        self.word = random.choice(word_list)

        #initialising the lists 
        self.word_guessed = []
        self.num_letters = 0
        
        for letter in self.word:
            self.word_guessed += "_"
            self.num_letters += 1

        self.num_lives = num_lives
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        """
        This function checks the guess against the chosen word. 
        
        Args:
            guess(str): the users guess.
        """
        #changes the guess to lower case
        self.guess = guess.lower()
        if self.guess in self.word:
            print(f"Good guess! {self.guess} is in the word.")
            for letter in self.word:
                if letter == self.guess:
                    #using index to replace underscore with the guess
                    ind = self.word.find(self.guess)
                    self.word_guessed[ind] = self.guess
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            print(f"Sorry, {self.guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
        
    def ask_for_input(self):
        """This function asks for an input and checks it is a single letter that has not been guessed before"""
        
        self.guess = input("Please enter a single letter:   ")
        if len(self.guess) != 1 or self.guess.isalpha == False:
            print("Invalid letter")
        elif self.guess in self.list_of_guesses:
            print("You've already tried this letter!")
        else:
            self.check_guess(self.guess)
            self.list_of_guesses.append(self.guess)

#all words have unique letters to make life easier
word_list = ["apricot", "peach", "mango", "grapes", "orange"]

def play_game(words):

    """This function plays the game of Hangman.
    
    Args:
        words(list): the list of words used for the hangman game.
    """
    num_lives = 5
    game = Hangman(words, num_lives)
    while True:
        if game.num_lives == 0:
            print("You've lost")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations! You've won!")
            break

play_game(word_list)