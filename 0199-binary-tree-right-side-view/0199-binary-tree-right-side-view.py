# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def smart(root,level):
            if not root:
                return 
            if len(ans)==level:
                ans.append(root.val)
            if root.right:
                smart(root.right,level+1)
            if root.left:
                smart(root.left,level+1)
        smart(root,0)
        return ans
        