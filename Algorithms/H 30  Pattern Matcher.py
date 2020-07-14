# noinspection SpellCheckingInspection
"""
Pattern Matcher
Given a String and a pattern ,we need to find if the string has the pattern.
Eg: String: gogopowerrangergogogogopowerranger
    Pattern: xxyxxy
    Here if we consider x: go   y: powerranger     then we find a match of pattern in the String.

"""


# O(N^2+M) Time / O(N+M) Space

def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []
    newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]
    counts = {"x": 0, "y": 0}
    firstYPos = getcountsAndFirstYPos(newPattern, counts)

    if counts['y'] != 0:
        for lenOfX in range(1, len(string)):
            lenOfY = (len(string) - lenOfX * counts['x']) / counts['y']
            if lenOfY <= 0 or lenOfY % 1 != 0:
                continue
            lenOfY = int(lenOfY)
            yIdx = firstYPos + lenOfX
            x = string[:lenOfX]
            y = string[yIdx:yIdx + lenOfY]
            potentialMatch = map(lambda char: x if char == 'x' else y, newPattern)
            if string == "".join(potentialMatch):
                return [x, y] if not didSwitch else [y, x]
    else:
        lenOfX = len(string) / counts['x']
        if lenOfX % 1 == 0:
            lenOfX = int(lenOfX)
            x = string[:lenOfX]
            potentialMatch = map(lambda char: x, newPattern)
            if string == "".join(potentialMatch):
                return [x, ""] if not didSwitch else ["", x]

    return []


def getNewPattern(pattern):
    patternLetters = list(pattern)
    if pattern[0] == "x":
        return patternLetters
    else:
        return list(map(lambda char: "x" if char == 'y' else 'y', patternLetters))


def getcountsAndFirstYPos(pattern, counts):
    firstYPos = None
    for i, char in enumerate(pattern):
        counts[char] += 1
        if char == 'y' and firstYPos == None:
            firstYPos = i
    return firstYPos
