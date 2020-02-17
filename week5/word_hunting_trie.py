"""
This version of word hunting replaced the isPrefix() and isWord() 
functions with a dictionary trie (built using the letters in dictionary) 
and the isChild function checking if the given letter is a child of 
the current node of trie.

The main idea is walking through the trie and the grid at same time.

This reduced the time complexity of checking prefix and word
from O(M) to O(1), where M is the number of words in the dictionary.
"""
from mytree import Node

def buildDictTrie(grid, dictionary, maxLen):
    """
    Create a trie using the words in dictionary, each node is a 
    letter, each branch with a termination mark is a word
    """
    root = Node(None, False)
    letters = set([letter for row in grid for letter in row])
    for word in dictionary:
        if (len(word) <= maxLen) and (len(set(word) - letters) == 0):
            currNode = root
            for i, letter in enumerate(word):
                # isTerminate defines if a word stops here
                isTerminate = i == (len(word)-1)
                newNode = Node(letter, isTerminate)
                nextNode = currNode.add_child(newNode)
                currNode = nextNode
    return root

def isChild(letter, node):
    """
    Returns if the given letter is a child of node of trie
    """
    currNode = node
    if letter in currNode.children.keys():
        return True, currNode.children[letter]
    return False, None

def isValidCoord(coord, size):
    """
    Returns if the coord is within the square of given size
    """
    return coord[0] >= 0 and coord[0] < size and \
        coord[1] >= 0 and coord[1] < size

def move(coord, direction):
    """
    Move the coord to the given direction, return the new coordinate
    """
    vInc, hInc = direction
    return (coord[0]+vInc, coord[1]+hInc)

def path_to_word(path, lettersGrid):
    """
    Returns a word corresponding to the path coordinates in grid
    """
    return ''.join([lettersGrid[coord[0]][coord[1]] for coord in path])

def dfs_on_grid(stack, size, maxLen, lettersGrid):
    dirs = [(i,j) for i in range(-1, 2) for j in range(-1, 2)]

    longestLen = 0
    longestPath = []

    while stack:
        currCoord, currPath, currNode = stack.pop()
        # if the path has no way to grow in any direction,
        # update longest path and length
        isGrowing = False
        for direction in dirs:
            newCoord = move(currCoord, direction)
            # check is the new coordinate is valid and not visited
            if (isValidCoord(newCoord, size) and \
                (newCoord not in currPath)):
                letter = lettersGrid[newCoord[0]][newCoord[1]]
                ischild, newNode = isChild(letter, currNode)
                if ischild:
                    newPath = currPath + [newCoord]
                    stack.append((newCoord, newPath, newNode))
                    isGrowing = True
                    if len(newPath) == maxLen:
                        return newPath
        if not isGrowing and len(currPath) > longestLen:
            longestLen = len(currPath)
            longestPath = currPath
    
    return longestLen, longestPath

def get_longest_word(lettersGrid, dictionary):
    """
    Returns the longest word can be found in the grid and dictionary by
    doing DFS on each cell in the grid
    """
    size = len(lettersGrid)
    maxLen = size*size
    
    trieRoot = buildDictTrie(lettersGrid, dictionary, maxLen)
    
    longestLen = 0
    longestPath = []
    for i in range(size):
        for j in range(size):      
            startCoord = (i,j)
            startPath = [startCoord]
            ischild, startNode = isChild(lettersGrid[i][j], trieRoot)
            if not ischild:
                continue
            startStack = [(startCoord, startPath, startNode)]
            currLen, currPath = dfs_on_grid(startStack, size, maxLen,
                lettersGrid)
            if currLen == maxLen:
                return path_to_word(currPath, lettersGrid)
            if currLen > longestLen:
                longestLen = currLen
                longestPath = currPath

    return path_to_word(longestPath, lettersGrid)