import random

import os


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.read().split(' ')
    f.close()

    secret_word = random.choice(words_list)
    return secret_word


# Worked together with Christopher Francisco to make this
#
# Please give me / him feedback on this if there is a more efficent way to do it.  He stores the list in a local variable
# and then just filters through that list instead of the entire file every time, which I assume is more efficent than the
# the way that I do it here.  But we would love to learn more if there is a cleaner way to do this.  Thank you!!
def get_new_word(current_word):
    # Open the file again as we are going to get a new word from the list
    with open('words.txt', 'r') as f:
        words_list = f.read().split(' ')

    # Oneline filter function that only gets words with a length of the current_word
    correct_len_words = filter(lambda x: len(
        x) == len(current_word), words_list)

    # Initalize a list for all the 'related' words in the list
    related_words = []
    # Loop through all the words in the length filtered list
    for word in list(correct_len_words):
        is_related = True  # Keep a variable to track related status of a letter
        # Get index and value for every letter in the current word
        for i, character in enumerate(current_word):
            if character.isalpha():  # Check if the character is alpha so that it ignores '_' characters
                # Set related to false if the letter in the word is not the same as the letter in current word
                if word[i] != character:
                    is_related = False
        if is_related:  # A check that will only add the word if related remains as true
            related_words.append(word)

    return related_words


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    ret = []
    for letter in secret_word:
        if letter in letters_guessed:
            ret.append(letter)
        else:
            ret.append('_')
    return ''.join(ret)


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    # for letter in secret_word:
    #     if letter == guess:
    #         return True

    # return False
    return [x for x in guess if x in secret_word]


def play_again():
    yes_or_no = input("Would you like to play again? y/n:  ")
    if "y".lower() in yes_or_no.lower():
        os.system('clear')
        return True
    else:
        os.system('clear')
        return False

# Helper funcs


def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    # Set the amount of incorrect guesses available to the length of the secret word
    incorrect_guesses = len(secret_word)

    # Welcome the user to spaceman and give them some info on the game they are going to be playing.  Also clear console :)
    os.system('clear')
    print('Welcome to spaceman!')
    print('The secret word contains: {} letters'.format(len(secret_word)))
    if is_palindrome(secret_word):
        print("Hint: The word is a palindrome")
    else:
        print("Hint: The word is not a panindrome")
    print('You have {} incorrect guesses left, please enter one letter per round'.format(
        incorrect_guesses))

    # Placeholders for use later in the program
    correct_guesses = []
    unused_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y', 'z']

    # Main game functionality
    while True:
        # Print to make it easier to read where you are in the program
        print('------------------------------ \n')

        # Check to see if they have won the game before doing anything else
        if is_word_guessed(secret_word, correct_guesses):
            print("Congrats!  You have won the game!")
            break

        # Check to see if their incorrect guesses is at 0
        if incorrect_guesses == 0:
            print("You lost the game.. Sorry about that")
            print("The answer was: {}".format(secret_word))
            break

        # Get user input
        letter = input("Enter a letter: ")

        # If the length of the the input is not 1 then it asks the user to try a new input
        if len(letter) != 1:
            print("Your input needs to be only one character, please try again")
            continue

        # Check to make sure that their input is only a letter
        if not letter.isalpha():
            print("Your input needs to be a letter of the alphabet, please try again")
            continue

        # If the letter is not in unused_letters (aka they have typed it before) then it asks them for a new input
        if letter not in unused_letters:
            print("You have already tried that input, please try again")
            continue

        # Remove the guessed letter from unused_letters and then make a remaining letters list for the user to see before any guess.
        unused_letters.remove(letter)
        remaining_letters = ','.join(unused_letters)

        # Check if the guess was correct or not
        if is_guess_in_word(letter, secret_word):
            # Add the letter to the correct guesses
            correct_guesses.append(letter)

            # Sets the secret word to a random word that contains the same 'characters' in the same spot.  This is for sinister spaceman
            secret_word = random.choice(get_new_word(get_guessed_word(secret_word, correct_guesses)))

            # Gets the new word with spots blanked out for things that they have not guessed so that it can be returned
            new_word = get_guessed_word(secret_word, correct_guesses)
            # Print information and where they are at in the game
            print("Your guess appears in the word!")
            print("Guessed word so far: {}".format(new_word))
            print("These letters you haven't guessed yet:  {}".format(
                remaining_letters))
        else:
            # Get the letters that they have so far
            guessed_word = get_guessed_word(secret_word, correct_guesses)

            # Remove one off of the incorrect guess counter
            incorrect_guesses -= 1

            # Print information and where they are at in the game
            print("Sorry, your guess was not in the word, try again")
            print("You have {} incorrect guesses left".format(
                incorrect_guesses))
            print("Guessed word so far: {}".format(guessed_word))
            print("These letters you haven't guessed yet:  {}".format(
                remaining_letters))


# These function calls that will start the game
running = True
while running:
    spaceman(load_word())
    running = play_again()