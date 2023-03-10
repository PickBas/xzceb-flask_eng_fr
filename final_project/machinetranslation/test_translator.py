import unittest

from translator import englishToFrench, frenchToEnglish


class TestMachineTranslation(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertEqual(englishToFrench("How are you?"), "Comment es-tu?")
        self.assertEqual(englishToFrench("Where are you?"), "Où es-tu?")
    
    def test_french_to_english(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertEqual(frenchToEnglish("Comment es-tu?"), "How are you?")
        self.assertEqual(frenchToEnglish("Où es-tu?"), "Where are you?")

if __name__ == '__main__':
    unittest.main()