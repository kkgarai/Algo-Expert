"""
Clone Trees

Given two Duplicate Binary Trees and a Node to search ,
Find the value from both the trees.
The trees contain the same values but don't have the same structure.
"""


def findNode(a, b, node):
    """
    :param a: Tree
    :param b: Tree
    :param node: Node
    :return: Value in the node
    """
    if a == node:
        return b
    if a.left and b.left:
        found = findNode(a.left, b.left, node)
        if found:
            return found
    if a.right and b.right:
        found = findNode(a.right, b.right, node)
        if found:
            return found
    return None
