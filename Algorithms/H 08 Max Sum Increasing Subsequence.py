"""
Max Sum Increasing Subsequence
Given a non-empty array we need to find the Max Sum of an Increasing Subsequence.
eg: array: [8,12,2,3,15,5,7]
    Sum:   8+12+15=35
    We also need to return [8,12,15] as they add up to the result.
"""


# O(n^2) time / O(n) space
def maxSumIncreasingSubsequence(array):
    sequences = [None for _ in array]
    sums = array[:]
    maxSumIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i

    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]


def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return sequence[::-1]
