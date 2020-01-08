#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 09:11:42 2020

@author: wenke_yang
"""

import collections

class MyIterator:
    """
    The MyIterator is a subclass of Python Iterator that supports the
    function of checking if there exists the next element.
    
    Attributes:
        myiter: a python iterator
        ------
        Private attributes:
        _has_next: if there exists an element to be iterated
        _next: next element to be iterated

    Methods:
        hasNext(): check if there is at least an element left to be iterated.
        next(): get the next element to be iterated. 
    """

    def __init__(self, myiter):
        """Initialise MyIterator object with given array/list/any data 
        structure that is iterable"""
        self.myiter = iter(myiter)
        self._has_next = None
        self._next = None
    
    def __iter__(self):
        return self

    def __next__(self):
        if self._has_next:
            result = self._next
        else:
            result = next(self.myiter)
        self._has_next = None
        return result

    def hasNext(self):
        if self._has_next is None:
            try:
                self._next = next(self.myiter)
            except StopIteration:
                self._has_next = False
            else:
                self._has_next = True
        return self._has_next