import unittest
from word_count import WordCount

class WordCountTestCase(unittest.TestCase):

    def test_zero(self):
        result = WordCount.counter(" ")
        self.assertEqual(result,0)
    def test_count(self):
        result = WordCount.counter("Python Library")
        self.assertEqual(result,2)


if __name__ == '__main__':
    unittest.main()

