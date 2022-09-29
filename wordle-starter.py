# import stuff up here
from random import choice
from logo import logo
import os
from colorama import Fore, Back, Style



class Wordle:
    def __init__(self, letters=5, logo=logo):
        self._letter = letters
        self._logo = logo
        self._guess = ''
        self._guesses = [[] for x in range(6)]
        self._tries = 0
        self._words = self.get_all_words()


    def get_all_words(self):
        # method to get all the words from the included file
        pass


    def chose_game_word(self):
        # method to pick a random word to play with
        pass


    def guess(self):
        # method to handle user input for guesses
        pass


    def play_game(self):
        # method to run the game logic (will call other methods)
        pass


    def update_display(self):
        # method to update the display in terminal on each guess
        pass


Wordle(5)
