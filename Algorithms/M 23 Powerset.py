"""
Powerset
P( [1,2,3] )=[ [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3] ]

"""


# (2^n * n) time / (2^n * n) space
def powerset(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets


# Recursive Solution

# (2^n * n) time / (2^n * n) space
def powerset(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset(array, idx - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets
