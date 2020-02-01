import unittest
from mytree import Node
from longest_path_in_tree_end_in import longest_path_in_tree

class TestLongestPathInTree(unittest.TestCase):
    def test_given1(self):
        """
        Tests the longest path start from root
        """
        test_tree = Node(1, [Node(2, [Node(4)]),
                             Node(3)])
        self.assertEqual(longest_path_in_tree(test_tree), 2,
            'Should be 2')

    def test_given2(self):
        """
        Tests the longest path ends in leaf
        """
        test_tree = Node(5, [Node(6),
                             Node(7, [Node(8, [Node(9, [Node(15),
                                                        Node(10)])]),
                                      Node(12)])])
        self.assertEqual(longest_path_in_tree(test_tree), 4,
            'Should be 4')

    def test_complex(self):
        """
        Tests a complex tree with some parents have three children.
        """
        test_tree = Node(1, [Node(2, [Node(8),
                                      Node(11),
                                      Node(13, [Node(14, [Node(15)])])]),
                             Node(10, [Node(3, [Node(4, [Node(5),
                                                         Node(7),
                                                         Node(12)]),
                                                Node(100)]),
                                      Node(12)])])
        self.assertEqual(longest_path_in_tree(test_tree), 3,
            'Should be 3')
    
    def test_middle(self):
        """
        Tests the longest path neither start from root nor end in leaf.
        """
        test_tree = Node(50, [Node(2, [Node(8),
                                      Node(11),
                                      Node(13)]),
                             Node(10, [Node(3, [Node(4, [Node(7),
                                                         Node(12)]),
                                                Node(20)]),
                                      Node(14)])])
        self.assertEqual(longest_path_in_tree(test_tree), 2,
            'Should be 2')    

if __name__ == '__main__':
    unittest.main()