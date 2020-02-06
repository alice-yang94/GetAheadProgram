import unittest
from word_hunting_trie import get_longest_word

GRID_SIZE = 4

class TestGetLongestWord(unittest.TestCase):

    def read_letters_grid(self, lettersFile):
        """
        Returns test letter grid (2D array) from testLetters.txt file
        """
        lettersGrid = [[0] * GRID_SIZE for i in range(GRID_SIZE)]
        with open(lettersFile) as file:
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    lettersGrid[i][j] = file.read(1)
        return lettersGrid

    def read_dictionary(self, dictFile):
        """
        Returns test dictionary, a set of words from testDict.txt file
        (choose set() because access is O(1))
        """
        dictionary = set()
        with open(dictFile) as file:
            for word in file:
                dictionary.add(word.strip('\n'))
        return dictionary

    def test_given1(self):
        lettersGrid1 = self.read_letters_grid('testLetters1.txt')
        dictionary = self.read_dictionary('testDict.txt')
        
        self.assertEqual(get_longest_word(lettersGrid1, dictionary), 
            'FAMES')

    def test_given2(self):
        lettersGrid2 = self.read_letters_grid('testLetters2.txt')
        dictionary = self.read_dictionary('testDict.txt')

        self.assertEqual(get_longest_word(lettersGrid2, dictionary), 
            'EMBOIL')

if __name__ == "__main__":
    unittest.main()