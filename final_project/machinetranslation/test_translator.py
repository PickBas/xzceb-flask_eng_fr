import unittest

from translator import english_to_french, french_to_english


class TestMachineTranslation(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("How are you?"), "Comment es-tu?")
        self.assertEqual(english_to_french("Where are you?"), "Où es-tu?")
        self.assertNotEqual(english_to_french("How are you?"), "Où es-tu?")
    
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Comment es-tu?"), "How are you?")
        self.assertEqual(french_to_english("Où es-tu?"), "Where are you?")
        self.assertNotEqual(french_to_english("Où es-tu?"), "How are you?")

if __name__ == '__main__':
    unittest.main()