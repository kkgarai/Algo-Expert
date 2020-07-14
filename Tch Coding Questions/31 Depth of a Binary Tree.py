"""
Depth of a Binary Tree


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        m x =0 q=[[root,1 ]]
        while q:
            x,l=q.pop( 0 )
            if x:
                mx=max(mx, l )
                q.append([x.left,l+1])
                q.append([x.right,l+1])

        return mx
