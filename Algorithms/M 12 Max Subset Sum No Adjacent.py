"""
Max Subset Sum No Adjacent
Given an array we need to find the greatest sum without adding two adjacent numbers in the array
The array contains only positive integers
Dynamic Programming

maxSum[i]=max{ maxSums[i-1],
               maxSums[i-2]+array[i] }

since we are only working with only two elements of maxSums , ie, maxSums[i-1] and maxSums[i-2]
so instead of using maxSums as an array we can just have two variables to store maxSums[i-1] and maxSums[i-2]
eg: array = [7,10,12,7,9,14]
MaxSum = 7+12+14=33

"""


# O(n) time / O(n) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
    return maxSums[-1]


# O(n) time / O(1) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first
