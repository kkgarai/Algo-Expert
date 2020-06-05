"""
Kadanes Algorithm
Given an array find the maximum subarray sum

Dynamic Programming

maxEndingHere=max(maxEndingHere + num , num)

"""

# O(n) time / O(1) space
def kadaneAlgorithm(array):
    """
    :param array: input array
    :return: maximum subarray sum
    """
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for num in array[1:]:
        maxEndingHere = max(maxEndingHere + num,num)
        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
    return maxSoFar
