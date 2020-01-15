#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:08:16 2020

@author: wenke_yang
"""

import unittest
"""
since Python does not support hasNext function, MyIterator is implemented
as the subclass of Python iterator with hasNext function in order to
test my FlattenedIterator class thoroughly.
"""
from myiterator import MyIterator
from flattenediterator_queue import FlattenedIterator

class TestFlattenedIterator(unittest.TestCase):

    def _list_to_iter(self, test_list):
        """
        helper function:
        converts list of arrays to list of iterators
        """
        iterators = []    
        for elem in test_list:
            iterators.append(MyIterator(elem))
        return iterators

    def test_interleaved_next(self):
        """
        test if the next() function can get next element in an 
        interleaved fashion.
        """
        test_list = [[1], [4,3], [6]]
        test_iter = self._list_to_iter(test_list)
        flattenedIter = FlattenedIterator(test_iter)

        self.assertEqual(next(flattenedIter), 1, "Should be 1")
        self.assertEqual(next(flattenedIter), 4, "Should be 4")
        self.assertEqual(next(flattenedIter), 6, "Should be 6")
        self.assertEqual(next(flattenedIter), 3, "Should be 3")

    def test_nonexistent_next(self):
        """
        test if the next() function can raise StopIteration exception
        when the next element is None
        """
        test_list = [[1], []]
        test_iter = self._list_to_iter(test_list)
        flattenedIter = FlattenedIterator(test_iter)
        next(flattenedIter)
        with self.assertRaises(StopIteration):
            next(flattenedIter)

    def test_hasNext(self):
        """
        test if the hasNext() function returns the existence of next 
        element correctly.
        """
        test_list = [[1], [], [6]]
        test_iter = self._list_to_iter(test_list)
        flattenedIter = FlattenedIterator(test_iter)

        self.assertEqual(flattenedIter.hasNext(), True, "Should be True")
        next(flattenedIter)
        self.assertEqual(flattenedIter.hasNext(), True, "Should be True")
        next(flattenedIter)
        self.assertEqual(flattenedIter.hasNext(), False, "Should be False")

    def test_empty_input(self):
        """
        test if the given list of iterators is empty 
        """
        test_iter = []
        flattenedIter = FlattenedIterator(test_iter)
        self.assertEqual(flattenedIter.hasNext(), False, "Should be False")
        with self.assertRaises(StopIteration):
            next(flattenedIter)

    def test_iterable(self):
        """
        test if the flattendIterator is iterable 
        (i.e. can be iterated using for loop)
        """
        test_list = [[1,2,3], 
                     [4,5], 
                     [6,7,8]]
        test_iter = self._list_to_iter(test_list)
        flattenedIter = FlattenedIterator(test_iter)
        self.assertEqual([elem for elem in flattenedIter], 
                         [1, 4, 6, 2, 5, 7, 3, 8], 
                         "Should be [1, 4, 6, 2, 5, 7, 3, 8]")

if __name__ == '__main__':
    unittest.main()