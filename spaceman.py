import random
import os
import re
import math
from colorama import Fore

# ACSII Ninja's best attempt lol
banner = '''
_______________________________________________________________ 
 _____                 _____             
|   __|___ ___ ___ ___|     |___ ___ ___ 
|__   | . | .'|  _| -_| | | | .'|   |   |
|_____|  _|__,|___|___|_|_|_|__,|_|_|_|_|
      |_|                                 
By: Ninjer27                        Art: @http://patorjk.com/       
________________________________________________________________
'''

spaceMan = [
    '''

        +---+
        |  |
        o  |
           |
           |
    |=======|
    ''',
    '''
        +---+
        |  |
        o  |
        |  |
           |
    |=======|

    ''',
    '''
        +---+
        |  |
        o  |
        |\ |
           |
    |=======|
    ''',
    '''
        +---+
        |  |
        o  |
       /|\ |
           |
    |=======|
    ''',
    '''
        +---+
        |  |
        o  |
       /|\ |
         \ |
    |=======|
    ''',
    '''
        +---+
        |  |
        o  |
       /|\ |
       / \ |
    |=======|
    '''
]







def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''

    for letters in secret_word:
        if letters in letters_guessed:
            return True
        else:
            return False
    


    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    return [x for x in guess if x in secret_word]


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    
    # Tell the User for normal instructions
    print(Fore.BLUE + banner + Fore.RESET)
    gameMode = input('Welcome to ' + Fore.BLUE + 'Spaceman' + Fore.RESET + '\nChoose a game mode:\n1. Normal Spaceman\n2. ' + Fore.RED + 'Illegal Spaceman\n' + Fore.RESET + 'Gamemode: ')
    
    # r'^[a-zA-Z]_'
    
    if re.match(r'^\d', gameMode):
        if int(gameMode) == 1:
            print('hi')
        elif int(gameMode) == 2:
            print('suffering')
        else:
            # induce true sufferin later 
            os.system('clear')
            print(Fore.RED + "Not an option".upper() + Fore.RESET)
            return spaceman(secret_word)
    else:
        os.system('clear')
        print(Fore.RED + "please put a valid respounce".upper() + Fore.RESET)
  
        return spaceman(secret_word)

    # print("\nRules are quite simple\n1. Guess One Letter at a time\n2. You run out of Guess you lose\n 3.Have Fun!!!")
    
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    
    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
spaceman(load_word())