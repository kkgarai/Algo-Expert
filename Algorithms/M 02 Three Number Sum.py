'''
Three Number Sum

Given a list, we need to find triplets whose sum is equal to a given number

'''


# O(n*2) time / O(n) space

def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right += 1
            elif currentSum < targetSum:
                left += 1
            else:
                right -= 1

    return triplets


array = list(map(int, input().split()))
targetSum = int(input())

print(threeNumberSum(array, targetSum))
