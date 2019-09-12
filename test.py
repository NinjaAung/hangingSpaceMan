import random
from colorama import Fore
import os

'''

Oh great TA or Teacher please don't grade this monstrocity

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
losing_space_man = [
    '''

        +---+
        |  |
  Press F For Respect
           |
           |
    |=======|
    '''
]
spaceMan.reverse()

def get_guess():
  
  # Set the dashes to the length of the secret word and set the amount of guesses 
  # the user has to 10
  
  dashes = "_" * len(secret_word)
  guesses_left = 7
  
  # This will loop as long as BOTH conditions are true:
  # 1. The number of guesses of left is greater than -1
  # 2. The dash string does NOT equal the secret word
  while guesses_left > -1 and not dashes == secret_word:
    
    # Print the amount of dashes and guesses left
    os.system('clear')
    spaceMan_number = int(guesses_left) - 1
    if spaceMan_number > -1:
        print( Fore.BLUE + spaceMan[int(spaceMan_number)] + Fore.RESET)
    else:
        print(Fore.RED + losing_space_man[0] + Fore.RESET)

    print(dashes)
    print (Fore.RED + str(guesses_left) + Fore.RESET)
    
    # Ask the user for input
    guess = input("Guess:")
    
    # Conditions that will print out a message according to
    # invalid inputs
    if len(guess) != 1:
      print ("Your guess must have exactly one character!")
      
    # If the guess is in the secret word then we updtae dashes to replace the
    # corresponding dash with the correct index the guess belongs to in the 
    # secret word
    elif guess in secret_word:
      print ("That letter is in the secret word!")
      dashes = update_dashes(secret_word, dashes, guess)
      
    # If the guess is wrong then we display a message and subtract
    # the amount of guesses the user has by 1
    else:
      print ("That letter is not in the secret word!")
      guesses_left -= 1
    
  if guesses_left < 0:
    print ("You lose. The word was: " + Fore.RED + str(secret_word) + Fore.RESET)
  
  # If the dash string equals the secret word in the end then the
  # user wins
  else:
    print ("Congrats! You win. The word was: " + Fore.RED + str(secret_word) + Fore.RESET)
    
# This function updates the string of dashes by replacing the dashes
# with words that match up with the hidden word if the user manages to guess
# it correctly
def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess     # Adds guess to string if guess is correctly
      
    else:
      # Add the dash at index i to result if it doesn't match the guess
      result = result + cur_dash[i]
      
  return result
    
words = ["Pneumonoultramicroscopicsilicovolcanoconiosis", "Supercalifragilisticexpialidocious", "Pseudopseudohypoparathyroidism", "Floccinaucinihilipilification", "Honorificabilitudinitatibus"]

secret_word = random.choice(words)
get_guess()