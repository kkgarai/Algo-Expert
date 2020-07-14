"""
Min Number Of Jumps
Given an array of the number of jumps available at that index.
We need to find the minumum number of jumps reqd. to reach the end.
eg : array: [3,4,2,1,2,3,7,1,1,1,3]
    Min Jumps: 4
    Jumps: index: 0 -> 1 -> 5 -> 6 -> 10
"""


# O(n^2) time / O(n) space
def minNumberOfJumps(array):
    jumps = [float('inf') for _ in array]
    jumps[0] = 0
    for i in range(1, len(array)):
        for j in range(i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[j] + 1, jumps[i])
    return jumps[-1]


# Solution 2 (tough/ better)
# O(n) time / O(n) space
def minNumberOfJumps(array):
    if len(array) == 1:
        return 0
    jumps = 0
    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i

    return jumps + 1
