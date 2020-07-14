"""
Numbers In Pi
We are given a string representation of first n digits of pi and a list of string representations of a few integers.
We need to find the minimum number of spaces we must add to the digits of pi so that all the remaining numbers are found in out list.

Dynamic Programming

eg: input: 3141592 [3141,5,31,2,4159,9,42]
    result: 2  Numbers Formed will be: 31,4159,2
"""


# O(N^3 + M) time / O(N+M) space
# Top Down Approach
def numbersInPi(pi, numbers):
    """
    :param pi: digits of pi (string)
    :param numbers: list of numbers ( list of strings)
    :return: min no of spaces
    """
    numbersTable = {number: True for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
    return -1 if minSpaces == float('inf') else minSpaces


def getMinSpaces(pi, numbersTable, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float('inf')
    for i in range(idx, len(pi)):
        prefix = pi[idx:i + 1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    return cache[idx]


# Bottom Up Approach
def numbersInPi(pi, numbers):
    """
        :param pi: digits of pi (string)
        :param numbers: list of numbers ( list of strings)
        :return: min no of spaces
        """
    numbersTable = {number: True for number in numbers}
    cache = {}
    for i in reversed(range(len(pi))):
        getMinSpaces(pi, numbersTable, cache, i)
    return -1 if cache[0] == float('inf') else cache[0]


def getMinSpaces(pi, numbersTable, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float('inf')
    for i in range(idx, len(pi)):
        prefix = pi[idx:i + 1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    return cache[idx]
