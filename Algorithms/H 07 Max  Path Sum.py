"""
Max  Path Sum
Given a Binary Tree we need to find the Maximun sum of any path.
A path is a collection of nodes that are connected and no node is connected to more than two nodes.
Note: We are given a Binary Tree NOT a BST.
eg:
                     1
                   /  \
                 2     3
               /  \   / \
             4    5  6  7

 Here paths are: [1,2,4], [4,2,5], [1,3,7], [6,3,7], [4,2,1,3,7], [5,2,1,3,6] etc
"""


# O(n) time / O(log(n)) space
def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)
    return maxSum


def findMaxSum(tree):
    if tree is None:
        return (0, 0)

    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)

    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = tree.value

    maxSumAsBranch = max(maxChildSumAsBranch + value, value)

    maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxChildSumAsBranch)
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

    return (maxSumAsBranch, maxPathSum)
