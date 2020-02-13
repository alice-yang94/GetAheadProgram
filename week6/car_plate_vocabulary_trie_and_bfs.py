from mytree import Node
import math

def build_dictionary_trie(vocabulary):
    vocabTrie = Node('Root', False)
    for word in vocabulary:
        currNode = vocabTrie
        for i, letter in enumerate(word):
            isTerminate = i == (len(word)-1)
            # To match the cases, all vocabulary letters are lower cased
            child = Node(letter.lower(), isTerminate)
            currNode = currNode.add_child(child)
    return vocabTrie

def extract_letters(plate):
    # To match the cases, all letters in plates are lower cased
    return ''.join([elem.lower() for elem in plate if elem.isalpha()])

def bfs_on_trie(vocabTrie, plateLetters, shortestWord, shortestLen):
    # queue stores node, current word and the letters haven't seen
    queue = [(vocabTrie, '', plateLetters)]
    while queue:
        currNode, currWord, currLetters = queue.pop(0)
        if len(currWord) >= shortestLen or shortestLen == 2:
            break
        if not currLetters and currNode.isTerminate:
            shortestWord = currWord
            shortestLen = len(currWord)
            break
        for child in currNode.children.values():
            newWord = currWord+child.val
            newLetters = currLetters
            if child.val in currLetters:
                newLetters = currLetters.replace(child.val, '', 1)
            queue.append((child, newWord, newLetters))

    return shortestWord, shortestLen

def get_shortest_words(vocabulary, licensePlates):
    shortestWord = '' 
    shortestLen = math.inf
    vocabTrie = build_dictionary_trie(vocabulary)

    for plate in licensePlates:
        plateLetters = extract_letters(plate)
        if len(plateLetters) >= shortestLen:
            continue
        shortestWord, shortestLen = bfs_on_trie(vocabTrie, plateLetters, 
            shortestWord, shortestLen)
        if shortestLen == 2:
            return shortestWord

    return shortestWord

