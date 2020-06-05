"""
Single Cycle Check
Given an array we need to check if it contains a single cycle.
i.e., we can return to the starting element after afer visitind all the elements exactly once.

the elements of the array  represent the jumps we can make,
eg: 2 : jump two steps forward
    -2: jump two steps backward
    3 : jump three steps forward
    -3: jump three steps backward

"""


# O(n) time / O(1) space
def singleCycleCheck(array):
    """
    :param array: input array
    :return: True / False
    """
    numElementsVisited = 0
    currentIdx = 0
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and currentIdx == 0:
            return False
        numElementsVisited += 1
        currentIdx = getNextIdx(currentIdx, array)
    return currentIdx == 0


def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)
