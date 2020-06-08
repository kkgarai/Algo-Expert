"""
Four Number Sum
Given an array and a target number, we need to find the quadruplet that add up to the target number.

"""


# O(n^2) time / O(n^2) space
def fourNumberSum(array, targetSum):
    allPairsSums = {}
    quadruplets = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairsSums:
                for pair in allPairsSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairsSums:
                allPairsSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairsSums[currentSum].append([array[k], array[i]])
    return quadruplets
