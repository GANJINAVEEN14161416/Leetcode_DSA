# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        stack=[]
        if not root:
            return None
        stack.append(root)
        while stack:
            pop=stack.pop()
            if pop.right:
                stack.append(pop.right)
            if pop.left:
                stack.append(pop.left)
            ans.append(pop.val)
        return ans
            
        