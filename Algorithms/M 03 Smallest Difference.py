"""
Smallest Difference
Given two arrays, we need to choose one number from each array such that their difference is the lowest among all the pairs that can be made bybbtaking one element from each array

"""


# O(nlog(n) +mlog(m)) time / 0(1) space
def smallestDifference(array1, array2):
    array1.sort()
    array2.sort()
    idx1 = 0
    idx2 = 0
    smallest = float('inf')
    current = float('inf')
    smallestPair = []
    while idx1 < len(array1) and idx2 < len(array2):
        firstNum = array1[idx1]
        secondNum = array2[idx2]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idx1 += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idx2+=1
        else:
            return [firstNum, secondNum]

        if current < smallest:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair


array1 = list(map(int, input().split()))
array2 = list(map(int,input().split()))
print(smallestDifference(array1,array2))

