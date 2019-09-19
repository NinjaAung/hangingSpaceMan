import spaceman
import test
import unittest
import re




''' User input checker using regex: Fail Case: None letter input'''
class regex_test(unittest.TestCase):
    def test_regex(self):
        self.assertRegex('a', r'^[a-zA-Z]*$', 'Letter passed regex')


''' Check if word was in fact loaded: Fail Case: Arg not passed resulting in a None'''
class word_loaded_test(unittest.TestCase):
    def test_load_word(self):
        self.assertIsNotNone(spaceman.load_word(), 'Word was loaded')


if __name__ == '__main__':
    unittest.main()