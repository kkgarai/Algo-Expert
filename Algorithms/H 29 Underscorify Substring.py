"""
Underscorify Substring
Given a string and a substring, we need to Underscorify all instances of  the substring from yje main string.
If the substrring is clubbed many times with itself then we Underscorify only the left and right end of it.
eg:
String: testthis is a testtest to see if testtesttest it works
Substring: test
Output: _test_this is a _testtest_ to see if _testtesttest_ it works
"""


# Solution
def solution(string, substring):
    return string.replace(substring, "_" + substring + "_").replace("__", "")


# OR

# O(N) time / O(N) space
def underscorifysubstring(string, substring):
    locations = collapse(getLocations(string, substring))
    return underscorify(string, locations)


def getLocations(string, substring):
    locations = []
    startIdx = 0
    while startIdx < len(string):
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            locations.append([nextIdx, nextIdx + len(substring)])
            startIdx = nextIdx + 1
        else:
            break

    return locations


def collapse(locations):
    if not len(locations):
        return locations
    newLocations = [locations[0]]
    previous = newLocations[0]
    for i in range(1, len(locations)):
        current = locations[i]
        if current[0] <= previous[1]:
            previous[1] = current[1]
        else:
            newLocations.append(current)
            previous = current
    return newLocations


def underscorify(string, locations):
    locationsIdx = 0
    stringIdx = 0
    inBetweenUnderscores = False
    finalChars = []
    i = 0
    while stringIdx < len(string) and locationsIdx < len(locations):
        if stringIdx == locations[locationsIdx][i]:
            finalChars.append("_")
            inBetweenUnderscores = not inBetweenUnderscores
            if not inBetweenUnderscores:
                locationsIdx += 1
            i = 0 if i == 1 else 1
        finalChars.append(string[stringIdx])
        stringIdx += 1
    if locationsIdx < len(locations):
        finalChars.append("_")
    elif stringIdx < len(string):
        finalChars.append(string[stringIdx:])
    return "".join(finalChars)
