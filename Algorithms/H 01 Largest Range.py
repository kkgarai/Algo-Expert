"""
Largest Range
Given an array  we need to find the largest range of numbers contained in it.
eg: [1,11,3,0,15,5,2,4,10,7,12,6] contains the range [0,7] as all the numbers from 0 to 7 are in this array.
    The range need not be contiguous in the array, but all the elements of the range must be present somewhere in the array.
    There may be many ranges but we need to return the longest one.

If we us the naive approach we may need O(n^2) time,
but we solve it using hash table.
"""


# O(n) time / O(n) space
def largestRange(array):
    bestRange = []
    longestLength = 0
    nums = {}

    for num in array:
        nums[num] = True

    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1

        while left in nums:
            nums[left] = False
            left -= 1

        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1

        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]

    return bestRange
