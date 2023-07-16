# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list1=[]
        def inorder(root):
            if not root:
                return
            list1.append(root.val)
            inorder(root.left)
            inorder(root.right)
            return root
        inorder(root)
        x=heapq.nsmallest(k,list1)
        return x[-1]
        