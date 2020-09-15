"""
Count Unival Subtrees

An Unival Subtrees is one in which all the nodes have the same value.
"""


def countUnivalSubtrees(root):
    count, isUnival = helper(root)
    return count


def helper(root):
    if not root:
        return 0, True
    leftCount, isLeftUnival = helper(root.left)
    righttCount, isRighttUnival = helper(root.right)

    if isLeftUnival and isRighttUnival and \
            root.left and root.right and \
            root.val == root.left.val and root.val == root.right.val:
        return leftCount + righttCount + 1

    return leftCount + righttCount, False
