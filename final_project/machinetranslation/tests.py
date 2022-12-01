import unittest

from translator import english_to_french,french_to_english

class TestEng(unittest.TestCase):

    def test_eng(self):
        self.assertEqual(english_to_french('null'),'Null')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        #Tests for English to French


class TestFr(unittest.TestCase):

    def test_fr(self):
        self.assertEqual(french_to_english('null'),'Null')
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        #Tests for French to English

unittest.main()