# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dic=defaultdict(int)
        ans=[]
        def solve(root,dic,ans):
            if not root:
                return ""
            s=str(root.val)+","+solve(root.left,dic,ans)+","+solve(root.right,dic,ans)
            dic[s]+=1
            if dic[s]==2:
                ans.append(root)
            return s
        solve(root,dic,ans)
        return ans
        