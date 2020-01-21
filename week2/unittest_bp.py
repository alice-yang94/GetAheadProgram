import unittest
from balanced_parentheses_stack import balanced_parentheses

#from balanced_parentheses_counter import balanced_parentheses

class TestBalancedParentheses(unittest.TestCase):
    def test_short_mixed(self):
        """
        Test if a short string of mixed good and bad parentheses works
        """
        test_parens = '())(())'
        self.assertEqual(balanced_parentheses(test_parens), 4, 
                        'Should be 4')

    def test_long_mixed(self):
        """
        Test if a long string of mixed good and bad parentheses works
        """
        test_parens = ')(()))))((((()'
        self.assertEqual(balanced_parentheses(test_parens), 4, 
                        'Should be 4')

    def test_empty(self):
        """
        Test if an empty string of parentheses works
        """
        test_parens = ''
        self.assertEqual(balanced_parentheses(test_parens), 0, 
                        'Should be 0')

    def test_non_parenthese(self):
        """
        Test if a string contains non-parenthese element would raise error
        """
        test_parens = '()o13'
        with self.assertRaises(ValueError):
            balanced_parentheses(test_parens)

    def test_all_good(self):
        """
        Test if a long all good string works
        """
        test_parens = '(((())))()()()((()))(())(()())'
        self.assertEqual(balanced_parentheses(test_parens), 30, 
                        'Should be 30')

    def test_given(self):
        """
        Tests given by Get Ahead Program
        """
        assert balanced_parentheses('') == 0
        assert balanced_parentheses('(') == 0
        assert balanced_parentheses(')') == 0
        assert balanced_parentheses('()(') == 2
        assert balanced_parentheses('())') == 2
        assert balanced_parentheses('(())') == 4
        assert balanced_parentheses('()()') == 4
        assert balanced_parentheses('()(()') == 2
        assert balanced_parentheses('(()())') == 6
        assert balanced_parentheses('())(())') == 4
        assert balanced_parentheses(')(()))))(((()') == 4
        assert balanced_parentheses('(()())((((()))))') == 16

if __name__ == '__main__':
    unittest.main()