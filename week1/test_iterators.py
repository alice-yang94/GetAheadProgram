#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:08:16 2020

@author: wenke_yang
"""
from myiterator import MyIterator
from flattenediterator_queue import FlattenedIterator
'''
# test my iterator     
myit = MyIterator([1,2,3])
while myit.hasNext():
    print(myit.next())
    
# test original iterator, should have throw StopIteration exception
it = iter([1,2,3]) 
while 1:
    try:
        print(next(it))
    except StopIteration:
        print('StopIteration Exception')
        break
'''

# cast list of arrays to list of iterators
def list_to_iter(test_list):
    iterators = []    
    for elem in test_list:
        iterators.append(MyIterator(elem))
    return iterators

test_list = [[1,2,3], 
             [4,5], 
             [6,7,8]]
#test_list = [[],[]]      
test_iter = list_to_iter(test_list) 

# test flattened iterator
'''    
flattenedIter = FlattenedIterator(test_iter)
while flattenedIter.hasNext():
    print(next(flattenedIter))
'''

test_iter = list_to_iter(test_list) 
flattenedIter2 = FlattenedIterator(test_iter)
for elem in flattenedIter2:
    print(elem)

fIter2 = iter(FlattenedIterator(list_to_iter(test_list)))
for elem in fIter2:
    print(elem)


'''
while 1:
    try:
        print(next(flattenedIter2))
    except StopIteration:
        print('StopIteration Exception')
        break
'''





