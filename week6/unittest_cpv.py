import unittest
from car_plate_vocabulary_trie_and_bfs import get_shortest_words
from car_plate_vocabulary_inverted_index import get_shortest_words

class TestShortestWords(unittest.TestCase):

    def read_strings(self, filename):
        """
        Returns a set of strings by reading them from the given file
        """
        strings = []
        with open(filename) as file:
            for word in file:
                strings.append(word.strip('\n'))
        return strings

    def test_given1(self):
        licensePlates = self.read_strings('testPlates.txt')
        vocabulary = self.read_strings('testVocab.txt')

        self.assertEqual(get_shortest_words(vocabulary, licensePlates),
            'car')
    
    def test_given2(self):
        licensePlates = ['RT123SO']
        vocabulary = self.read_strings('testVocab.txt')

        self.assertEqual(get_shortest_words(vocabulary, licensePlates),
            'sort')

if __name__ == "__main__":
    unittest.main()