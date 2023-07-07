# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', n1: 'TreeNode', n2: 'TreeNode') -> 'TreeNode':
        def solve(root):
            if not root or root==n2 or root==n1:
                return root
            l=solve(root.left)
            r=solve(root.right)
            if not l:
                return r
            elif not r:
                return l
            else:
                return root
        return solve(root)
        