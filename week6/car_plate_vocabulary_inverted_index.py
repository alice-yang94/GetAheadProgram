import math
from collections import defaultdict

def build_inverted_index(vocabulary):
    """
    Returns an inverted index of the given vocabulary, keys are letters,
    values are set of words that contains its key
    """
    invertedIndex = defaultdict(set)
    for word in vocabulary:
        # To match the cases, all letters in vocabulary are lower cased
        for letter in word.lower():
            invertedIndex[letter].add(word)
    return invertedIndex

def extract_letters(plate):
    """Returns all letters contained in the plate. To match the cases,
    all letters are lower cased"""
    plateLetters = defaultdict(int)
    for elem in plate:
        if elem.isalpha():
            plateLetters[elem.lower()] += 1
    return plateLetters

def check_count(plateLetters, commonWords):
    """Returns the commonWords that meets the required count"""
    for letter, count in plateLetters.items():
        if count > 1:
            commonWords = {word for word in commonWords 
                if word.count(letter) >= count}
    return commonWords

def get_common_words(plateLetters, invertedIndex):
    """Returns the words that includes all unique letters in a plate"""
    # intersect letters with smaller word count first 
    # to reduce the intermediate result size
    letters = sorted(plateLetters.keys(),key=lambda x:len(invertedIndex[x]))
    commonWords = invertedIndex[letters[0]]
    for letter in letters[1:]:
        containsLetter = invertedIndex[letter]
        commonWords = commonWords.intersection(containsLetter)
        if not commonWords:
            break
    return commonWords

def get_shortest_words(vocabulary, licensePlates):
    """
    Returns a shortest word that contains all letters in a plate that
    exists in the vocabulary
    """
    shortestWord = ''
    shortestLen = math.inf
    invertedIndex = build_inverted_index(vocabulary)

    for plate in licensePlates:
        plateLetters = extract_letters(plate)
        commonWords = get_common_words(plateLetters, invertedIndex)
        commonWords = check_count(plateLetters, commonWords)
        if not commonWords:
            continue
        currShortestWord = min(commonWords, key=len)
        currShortestLen = len(currShortestWord)
        if currShortestLen == 2:
            # the min len is 2 because a plate at least got 2 letters
            return currShortestWord
        if currShortestLen < shortestLen:
            # update shortest word and its length
            shortestLen = currShortestLen
            shortestWord = currShortestWord

    return shortestWord