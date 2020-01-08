#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 09:40:51 2020

@author: wenke_yang
"""

class FlattenedIterator:
    """
    The FlattenedIterator incrementally iterates over the integers from all 
    the iterators in an interleaved fashion.
    
    Attributes:
        iterators: a given list of iterators
        ------
        Private attributes:
        _len: the length of iterators
        _curr_idx: the current index of iterators that has been iterated to
        _has_next: if there exists an element to be iterated
        _next: next element to be iterated

    Methods:
        __iter__():
        __next__(): get the next interleaved element to be iterated.
        hasNext(): check if there is at least an element from all iterators
        that is left to be iterated. 
    """
    
    def __init__(self, iterators):
        """
        Initialise FlattenedIterator class with a given list of iterators,
        the length of iterators, zero as the start current index, 
        the next element and its existence are unknown unless calling 
        hasNext() function
        """
        self.iterators = iterators
        self._len = len(iterators)
        self._curr_idx = 0
        self._has_next = None
        self._next = None
        
    def __iter__(self):
        """
        Returns the FlattenedIterator itself.
        """
        return self

    def __next__(self):
        """
        Returns the next interleaved element from iterators. 
        Raises StopIteration Exception if next element is not available 
        """
        if self.hasNext() and self._curr_idx < self._len:
            next_elem = self._next
        else:
            raise StopIteration
            
        """update current index to next iterator and reset info. of next element"""
        self._curr_idx += 1        
        self._has_next = None
        self._next = None
        return next_elem

    def hasNext(self):
        """
        Returns True if there is an element has not been iterated from any
        of the iterators, else, returns False.
        """
        if self._has_next is None:
            self._has_next = False
            """traverse all iterators start from the current index until next
            element found"""
            start = self._curr_idx
            end = self._curr_idx + self._len
            for i in range(start, end):
                """mod the index with length to deal with index out of range"""
                curr_idx = i % self._len
                curr_iter = self.iterators[curr_idx]
                if curr_iter.hasNext():
                    self._curr_idx = curr_idx
                    self._has_next = True
                    self._next = next(self.iterators[curr_idx])
                    break       
        return self._has_next