import unittest
from histograms_and_areas import get_largest_area

class TestLargestAreas(unittest.TestCase):

    def test_given1(self):
        """
        Test case given by GetAheadProgram
        """
        inputArray = [2,4,2,1]
        sol = (6, (0,2))
        self.assertEqual(get_largest_area(inputArray), sol, 
            f'The max area should be {sol[0]}' +
            f'The indices are {sol[1]}')

    def test_given2(self):
        """
        Test case given by GetAheadProgram
        """
        inputArray = [2,4,2,1,10,6,10]
        sol = (18, (4,6))
        self.assertEqual(get_largest_area(inputArray), sol, 
            f'The max area should be {sol[0]}' +
            f'The indices are {sol[1]}')

    def test_flat(self):
        """
        Tests if the longest area is the lowest value run through the 
        inputArray, in this case, value 1 from first index to the last 
        index
        """
        inputArray = [1,2,2,1,1,2,2,1]
        sol = (8, (0,7))
        self.assertEqual(get_largest_area(inputArray), sol, 
            f'The max area should be {sol[0]}' +
            f'The indices are {sol[1]}')

    def test_empty(self):
        """
        Tests if the input array is None
        """
        inputArray = []
        sol = (0, None)
        self.assertEqual(get_largest_area(inputArray), sol, 
            f'The max area should be {sol[0]}' +
            f'The indices are {sol[1]}')

    def test_zero(self):
        """
        Tests if the input array is None
        """
        inputArray = [0,2,1,2,1]
        sol = (4, (1,4))
        self.assertEqual(get_largest_area(inputArray), sol, 
            f'The max area should be {sol[0]}' +
            f'The indices are {sol[1]}')


if __name__ == "__main__":
    unittest.main()