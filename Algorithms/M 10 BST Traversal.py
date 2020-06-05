"""
Binary SearchbTree Traversal
In-order Traversal
Pre-order Traversal
Post-order Traversal

"""

# O(n) time / O(n) space
def inOrderTraverse(tree, array):
    """
    tree is the binary tree and the result of traversal will be stored in ihe array
    """
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


# O(n) time / O(n) space
def preOrderTraverse(tree, array):
    """
    tree is the binary tree and the result of traversal will be stored in ihe array
    """
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


# O(n) time / O(n) space
def postOrderTraverse(tree, array):
    """
    tree is the binary tree and the result of traversal will be stored in ihe array
    """
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array
