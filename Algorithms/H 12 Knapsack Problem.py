"""
Knapsack Problem
Given a list of lists representing the weights and values of items, and an integer representing the Knapsack capacity.
We need to maximize our profit.
We must consider items as whole numbers(not fractions).
eg: input: [[1,2],[4,3],[5,6],[6,7]], 10
    result: 10 [[6,7],[4,3]]
"""


# O(N*C) time / O(N*C) space
# where N: no. of items,    C: capacity of our bag
def knapsackProblem(items, capacity):
    knapsackValues = [[0 for x in range(capacity + 1)] for y in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        currentValue, currentWeight = items[i - 1]
        for c in range(capacity + 1):
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                knapsackValues[i][c] = max(knapsackValues[i - 1][c],
                                           knapsackValues[i - 1][c - currentWeight] + currentValue)
    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]


def getKnapsackItems(knapsackValues, items):
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1
    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(items[i - 1])
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))
