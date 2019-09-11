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
           |
           |
           |
    |=======|
    ''',
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

    secret = []
    for letter in secret_word:
        if letter in letters_guessed:
            secret.append(letter)
        else:
            secret.append('_')
    return ''.join(secret)


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''


    return [x for x in guess if x in secret_word]

def play_again():
    yes_or_no = input("Would you like to play again? y/n:  ")
    if "y".lower() in yes_or_no.lower():
        os.system('clear')
        return True
    else:
        os.system('clear')
        return False

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

    incorrect_guesses = 7
    spaceMan_number = int(incorrect_guesses) - 1

    correct_guesses = []
    unused_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    if re.match(r'^\d', gameMode):
        if int(gameMode) == 1:
            os.system('clear')
            print(spaceMan[int(spaceMan_number)])
            print('The word is {} letters long     ||      You have {} guesses left'.format(len(secret_word), incorrect_guesses))
            print()
            while True:
                print('-' * 8)
                letter_input = input('Guess a letter: ')

                if len(letter_input) != 1 or letter_input.isalpha() or re.match(r'^\d', letter_input):
                    print("Only one letter character only, or you'll be hanged") # \' present in the text 
                    continue
                

                if letter_input not in unused_letters:
                    print('You have already tried that input, please try again')
                    continue

                if incorrect_guesses == 0:
                    print('Looks like you dead chief')
                    print('The answer was: {}'.format(secret_word))
                    break

                if is_word_guessed(secret_word, correct_guesses):
                    print("Congrats!  You're not dead") # \' present in the text
                    break

                if letter_input not in unused_letters:
                    print('You have already tried that input, please try again')
                    continue

                unused_letters.remove(letter_input)

                if is_guess_in_word(letter_input, secret_word):
                    correct_guesses.append(letter_input)

                    new_word = get_guessed_word(secret_word, correct_guesses)
                    print('another one!\nWord: {}'.format(new_word))
                else:
                    incorrect_guesses -= 1
                    guessed_word = get_guessed_word(secret_word, correct_guesses)
                    print("Sorry, your guess was not in the word, try again")
                    print("You have {} incorrect guesses left".format(incorrect_guesses))
                    print("Guessed word so far: {}".format(guessed_word))

                    
                
                
            
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






#These function calls that will start the game
running = True
while running:
    spaceman(load_word())
    running = play_again()