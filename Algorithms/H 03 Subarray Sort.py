"""Subarray Sort Given an array of atleast two elements, we need to find the smallest subarray from it which,
    when sorted, will make the entire array sorted.

"""


# O(n) time / O(1) space
def subarraySort(array):
    minOutOfOrder = float('inf')
    maxOutOfOrder = -float('inf')

    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)

    if minOutOfOrder == float('inf'):
        return [-1, -1]

    subarrayLeftIdx = 0
    while minOutOfOrder > array[subarrayLeftIdx]:
        subarrayLeftIdx += 1
    subarrayRighttIdx = len(array) - 1
    while maxOutOfOrder < array[subarrayRighttIdx]:
        subarrayRighttIdx -= 1
    return [subarrayLeftIdx, subarrayRighttIdx]


def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]

    return num > array[i + 1] or num < array[i - 1]
