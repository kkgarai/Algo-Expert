"""
Water Area
Given an array representing the height of walls/pillars,
we need to find the amount of water that can be stored in b/w those pillars/walls.
eg: heights: [0,8,0,0,5,0,0,10,0,0,1,1,0,3]
    Water Area: 48
"""

# O(N) time / O(N) space  actually 3*n time and space
def waterArea(array):
    leftMax = [_ for _ in array]
    rightMax = [_ for _ in array]
    waterArea = 0
    for i in range(1, len(array)):
        leftMax[i] = max(leftMax[i], leftMax[i - 1])
    for i in reversed(range(len(array) - 1)):
        rightMax[i] = max((rightMax[i], rightMax[i + 1]))
    for i, ht in enumerate(array):
        waterArea += min(leftMax[i], rightMax[i]) - ht
    return waterArea
