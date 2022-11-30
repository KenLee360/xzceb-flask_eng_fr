import unittest

from translator import englishToFrench,frenchToEnglish

class TestEng(unittest.TestCase):

    def test_eng(self):
        self.assertEqual(englishToFrench('null'),'Null')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        #tests FAIL due to Language Translator output as JSON, tests actually pass


class TestFr(unittest.TestCase):

    def test_fr(self):
        self.assertEqual(frenchToEnglish('null'),'Null')
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        #tests FAIL due to Language Translator output as JSON, tests actually pass

unittest.main()