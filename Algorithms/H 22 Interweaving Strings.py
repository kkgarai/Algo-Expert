"""
Interweaving Strings

Given two strings and a target string, can the two strings be interweaved to get the target string.

Interweaving: merging two strings in a way thet their letters appear in order, though they may not be adjacent in theit final string.
eg: ab and cd can be interweaved as : abcd, cdab, acbd, cadb.

eg :   strings: aaa,aaaf
       target: aaafaaa
       result: True (as aaaf + aaa = aafaaa)

Dynamic Programming
"""


# O(2^(N+M)) time / O(N+M) space
# Recursive solution
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    return areInterwoven(one, two, three, 0, 0)


def areInterwoven(one, two, three, i, j):
    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        if areInterwoven(one, two, three, i + 1, j):
            return True

    if j < len(two) and two[j] == three[k]:
        return areInterwoven(one, two, three, i, j + 1)

    return False


# Dynamic Solution
# O(NM) time / O(NM) space
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    cache = [[None for j in range(len(two) + 1)] for i in range(len(one) + 1)]
    return areInterwoven(one, two, three, 0, 0, cache)


def areInterwoven(one, two, three, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]
    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i + 1, j, cache)
        if cache[i][j]:
            return True

    if j < len(two) and two[j] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i, j + 1, cache)
        return cache[i][j]

    cache[i][j] = False

    return False
