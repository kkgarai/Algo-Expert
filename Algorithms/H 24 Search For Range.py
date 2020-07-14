"""
Search For Range

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target
value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


"""


# Recursive solution
# O(log(n)) time / O((1)) space
def searchForRange(array, target):
    finalRange = [-1, -1]
    binarySearchAltered(array, target, 0, len(array) - 1, finalRange, True)
    binarySearchAltered(array, target, 0, len(array) - 1, finalRange, False)
    return finalRange


def binarySearchAltered(array, target, left, right, finalRange, goLeft):
    if left > right:
        return
    mid = (left + right) // 2
    if array[mid] < target:
        binarySearchAltered(array, target, mid + 1, right, finalRange, goLeft)
    elif array[mid] > target:
        binarySearchAltered(array, target, left, mid - 1, finalRange, goLeft)
    else:
        if goLeft:
            if mid == 0 or array[mid - 1] != target:
                finalRange[0] = mid
            else:
                binarySearchAltered(array, target, left, mid - 1, finalRange, goLeft)
        else:
            if mid == len(array) - 1 or array[mid + 1] != target:
                finalRange[1] = mid
            else:
                binarySearchAltered(array, target, left, mid + 1, finalRange, goLeft)


# Iterative Solution

def searchForRangeIterative(array, target):
    finalRange = [-1, -1]
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, True)
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, False)
    return finalRange


def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
    while left <= right:

        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            if goLeft:
                if mid == 0 or array[mid - 1] != target:
                    finalRange[0] = mid
                    return
                else:
                    right = mid - 1
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    finalRange[1] = mid
                    return
                else:
                    left = mid + 1
