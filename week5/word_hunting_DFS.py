"""
Note:
This version of DFS store all visited path for each current node,
has higher space complexity O(n^2), where n is the number of cells in grid.

Store a global visited path and store parent coordinate for each current
node, pop to the parent coordinate can reduce the space complexity 
to O(n)
"""

def isPrefix(string, dictionary):
    """
    Returns if the given string is a prefix of any word in the dictionary

    Args:
        string: a string of characters
        dictionary: a set of words
    """
    strLen = len(string)
    for word in dictionary:
        if word[:strLen] == string:
            return True
    return False

def isWord(word, dictionary):
    """
    Returns if the given word exists in the dictionary

    Args:
        word: a string of characters
        dictionary: a set of words
    """
    return word in dictionary

def isValidCoord(coord, size):
    """
    Returns if the coord is within the square of given size
    """
    return coord[0] >= 0 and coord[0] < size and \
        coord[1] >= 0 and coord[1] < size

def dirToIncrement(direction):
    """
    Returns the shifts in vertical and horizontal by giving direction
    """
    # assume upperleft corner is (0,0)
    if direction == 'up':
        return (0,-1)
    elif direction == 'down':
        return (0,1)
    elif direction == 'left':
        return (-1,0)
    elif direction == 'right':
        return (1,0)
    vertical, horizontal = direction.split()
    v1, h1 = dirToIncrement(vertical)
    v2, h2 = dirToIncrement(horizontal)
    return (v1+v2, h1+h2)

def move(coord, direction):
    """
    Move the coord to the given direction, return the new coordinate
    """
    vInc, hInc = dirToIncrement(direction)
    return (coord[0]+vInc, coord[1]+hInc)

def path_to_word(path, lettersGrid):
    """
    Returns a word corresponding to the path coordinates in grid
    """
    return ''.join([lettersGrid[coord[0]][coord[1]] for coord in path])

def dfs_on_grid(stack, size, maxLen, lettersGrid, dictionary):
    """
    Dfs on the grid with given start status in stack

    Args: 
        stack: a stack with start coordinate and path
        size: width of the grid
        maxLen: the total number of cells in the grid
        lettersGrid: a grid of letters
        dictionary: a set of words

    Returns:
        longestLen: the longest path length if start at given status
        longestPath: the longest path if start at given status
    """
    dirs = ['up', 'down', 'left', 'right',
            'up left', 'up right', 'down left', 'down right']
    longestLen = 0
    longestPath = []

    while stack:
        currCoord, currPath = stack.pop()
        # if the path has no way to grow in any direction,
        # update longest path and length
        isGrowing = False
        for direction in dirs:
            newCoord = move(currCoord, direction)
            # check is the new coordinate is valid and not visited
            if (isValidCoord(newCoord, size) and \
                (newCoord not in currPath)):
                newPath = currPath + [newCoord]
                word = path_to_word(newPath, lettersGrid)
                # check isWord first because the set access time is O(1),
                # while the average time complexity of isPrefix is O(n)
                if isWord(word, dictionary) or isPrefix(word, dictionary):
                    stack.append((newCoord, newPath))
                    isGrowing = True
                    if len(newPath) == maxLen:
                        return newPath
        if not isGrowing and len(currPath) > longestLen:
            longestLen = len(currPath)
            longestPath = currPath
    
    return longestLen, longestPath

def filterDict(lettersGrid, dictionary, maxLen):
    """
    Returns a filtered dictionary, removed all words with letters not in
    the grid and those longer than max possible length or smaller than
    3 letters
    """
    letters = set([letter for row in lettersGrid for letter in row])
    return set([word for word in dictionary if (len(word) <= maxLen) and
        (len(word) >= 3) and (len(set(word) - letters) == 0)])

def get_longest_word(lettersGrid, dictionary):
    """
    Returns the longest word can be found in the grid and dictionary by
    doing DFS on each cell in the grid

    Args:
        lettersGrid: a gird of letters
        dictionary: a set of words
    """
    size = len(lettersGrid)
    maxLen = size*size
    # pruning: filter impossible words in the dictionary
    newDict = filterDict(lettersGrid, dictionary, maxLen)

    longestLen = 0
    longestPath = []
    for i in range(size):
        for j in range(size):      
            startCoord = (i,j)
            startPath = [startCoord]
            startStack = [(startCoord, startPath)]
            # find longest path with each start cell, and update longest
            # length and path
            currLen, currPath = dfs_on_grid(startStack, size, maxLen,
                lettersGrid, newDict)
            if currLen == maxLen:
                return path_to_word(currPath, lettersGrid)
            if currLen > longestLen:
                longestLen = currLen
                longestPath = currPath

    # convert coordinates to letters before returning
    return path_to_word(longestPath, lettersGrid)