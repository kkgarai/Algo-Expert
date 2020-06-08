"""
Min Rewards

Given an array of scores of a test in the order of their seating arrangements.
We need to find the minimum number of rewards required to give the students.
The rewards are distributed based on the following criteria:
    -> Every student must have atleast one reward.
    -> If a student has higher marks than the one adjacent to him, then his rewards should also be more.
Note: There may be duplicate values in the array.

eg: scores: [8,4,2,1,3,6,7,9,5] then
    rewards: [4,3,2,1,2,3,45,1]
    minRewards: 25
"""


# Solution 1
# O(n^2) time / O(n) space
def minRewards(scores):
    rewards = [1 for _ in scores]

    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1
    return sum(rewards)






# Solution 2
# O(n) time / O(n) space
def minRewards(scores):
    rewards = [1 for _ in scores]
    localMinIdxs = getLocalMinIdx(scores)
    for localMinTdx in localMinIdxs:
        expandFromLocalMinIdx(localMinTdx, scores, rewards)
    return sum(rewards)


def getLocalMinIdx(array):
    if len(array) == 1:
        return array[0]
    localMinIdxs = []
    for i in range(len(array)):
        if i == 0 and array[i] < array[i + 1]:
            localMinIdxs.append(i)
        if i == len(array) - 1 and array[i] < array[i - 1]:
            localMinIdxs.append(i)
        if i == 0 or i == len(array) - 1:
            continue
        if array[i] < array[i + 1] and array[i] < array[i - 1]:
            localMinIdxs.append(i)
    return localMinIdxs


def expandFromLocalMinIdx(localMinIdx, scores, rewards):
    leftIdx = localMinIdx - 1
    while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
        rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
        leftIdx -= 1
    rightIdx = localMinIdx + 1
    while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1]:
        rewards[rightIdx] = rewards[rightIdx - 1] + 1
        rightIdx += 1








# Solution 3 (Most Efficient)
# O(n) time / O(n) space
def minRewards(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)
