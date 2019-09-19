import spaceman
import test
import unittest
import re




''' User input checker using regex: Fail Case: None letter input'''
class regex_test(unittest.TestCase):
    '''
    A function that read user input for a given _ = input('_') and checks if it everything 
        but singular letter.
    Returns:
        bool: True if it's a singular letter, False otherwise
    '''

    def test_regex(self):
        self.assertRegex('a', r'^[a-zA-Z]*$', 'Letter passed regex')


''' Check if word was in fact loaded: Fail Case: Arg not passed resulting in a None'''
class word_loaded_test(unittest.TestCase):

    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''

    def test_load_word(self):
        self.assertIsNotNone(spaceman.load_word(), 'Word was loaded')


''' Check if word was guessed properly in both cases guessed_word and guess_in_word'''
class test_guessed_word(unittest.TestCase):

    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    def test_guessed_word(self): #tests to see if letters guessed are in word
        assert spaceman.get_guessed_word(("halloween"), ['a', 'l', 'e', 'n']) == "_all__een"
        assert spaceman.get_guessed_word(("halloween"), ['h','w', 'e', 'x']) == "h____wee_"

    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''

    def test_is_guess_in_word(self): #tests to see if user letter guessed is correct
        assert spaceman.is_guess_in_word(("a"), ('art')) is True
        assert spaceman.is_guess_in_word(("b"), ('art')) is False



if __name__ == '__main__':
    unittest.main()