import spaceman
import unittest
import re

''' User input checker using regex: Fail case: None letter input'''
class RegexCheckTest(unittest.TestCase):

    def test_regex(self):
        self.assertRegex('a', r'^[a-zA-Z]*$', 'Letter passed regex')


if __name__ == '__main__':
    unittest.main()