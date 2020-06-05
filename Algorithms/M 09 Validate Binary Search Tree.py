"""
Validate Binary Search Tree
Given a Binary Tree , we need to check whether or not it is a BST

"""


# O(n) time / O(d) space

def validate(tree):
    return validateBstHelper(tree, float('inf'), float('inf'))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value > maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)
