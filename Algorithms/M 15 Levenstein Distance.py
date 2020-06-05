"""
Levenstein Distance
Given a string we need to find the minimum no of operations to make it equal to another string
Operations are : insertion,deletion and substitution

Dynamic Programming

if str1[r] == str[2] : E[r][c] = E[r-1][c-1]
else : E[r][c] = 1 + min( E[r][c-1],E[r-1][c],E[r-1][c-1])

"""


# O(n*m) time / O(n*m) space
# where n and m are the lengths of the two strings
def levenshteinDistance(str1, str2):
    """
    :param str1: input string
    :param str2: input string
    :return: Levenstein Distance
    """
    str1 = " " + str1
    str2 = " " + str2
    result = [[0 for col in range(len(str2))] for row in range(len(str1))]
    for r in range(len(str1)):
        for c in range(len(str2)):
            if r == 0:
                result[r][c] = c
            elif c == 0:
                result[r][c] = r
            else:
                if str1[r] == str2[c]:
                    result[r][c] = result[r - 1][c - 1]
                else:
                    result[r][c] = 1 + min(result[r][c - 1], result[r - 1][c], result[r - 1][c - 1])

    return result[len(str1) - 1][len(str2) - 1]


# O(n*m) time / O(min(n,m)) space
# where n and m are the lengths of the two strings

def levenshteinDistance(str1, str2):
    """
        :param str1: input string
        :param str2: input string
        :return: Levenstein Distance
        """
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    evenEdits = [x for x in range(len(small) + 1)]
    oddEdits = [x for x in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = i
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                currentEdits[j] = previousEdits[j - 1]
            else:
                currentEdits[j] = 1 + min(previousEdits[j - 1], previousEdits[j], currentEdits[j - 1])
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]
