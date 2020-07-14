"""
Shifted Binary Search


Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


# Recursive solution
# O(log(n)) time / O(log(n)) space
def shiftedBinarySearchRecursive(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)


def shiftedBinarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potentialMatch = array[middle]

    leftNum = array[left]
    rightNum = array[right]

    if target == potentialMatch:
        return middle

    elif leftNum <= potentialMatch:
        if target < potentialMatch and target >= leftNum:
            return shiftedBinarySearchHelper(array, target, left, middle - 1)
        else:
            return shiftedBinarySearchHelper(array, target, middle + 1, right)
    else:
        if target > potentialMatch and target <= rightNum:
            return shiftedBinarySearchHelper(array, target, middle + 1, right)
        else:
            return shiftedBinarySearchHelper(array, target, left, middle - 1)


# Iterative Solution
# O(log(n)) time / O(1) space
def shiftedBinarySearchIterative(array, target):
    return shiftedBinarySearchIterativeHelper(array, target, 0, len(array) - 1)


def shiftedBinarySearchIterativeHelper(array, target, left, right):
    while left < right:
        middle = (left + right) // 2
        potentialMatch = array[middle]

        leftNum = array[left]
        rightNum = array[right]

        if target == potentialMatch:
            return middle

        elif leftNum <= potentialMatch:
            if target < potentialMatch and target >= leftNum:
                right = middle - 1

            else:
                left = middle - 1

        else:
            if target > potentialMatch and target <= rightNum:
                left = middle + 1

            else:
                right = middle - 1

    return -1
