"""
Invert Binary Tree
Given a binary tree we need to create a sideways mirror image of the tree.
The parent-children relationships remain the same but the sides are changed ,i.e. left and right  chindren are swapped

"""


# O(n) time / O(n) space
def invertBinaryTree(tree):
    """
    Iterative solution
    """
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)


def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left


# O(n) time / O(d) space
def invertBinaryTree(tree):
    """
    Recursive solution
    """
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
