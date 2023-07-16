# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', n1: 'TreeNode', n2: 'TreeNode') -> 'TreeNode':
        
        def LCA1(root, n1, n2):
            if not root:
                return 
            cur=root
            if n1.val<cur.val and n2.val>cur.val:
                return cur
            elif n1.val<cur.val and n2.val<cur.val:
                return LCA1(root.left,n1,n2)
            elif n1.val>cur.val and n2.val>cur.val:
                return LCA1(root.right,n1,n2)
            return root
        return LCA1(root,n1,n2)