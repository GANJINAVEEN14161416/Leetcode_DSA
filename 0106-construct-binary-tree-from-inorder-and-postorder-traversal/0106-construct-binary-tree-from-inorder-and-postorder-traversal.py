# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic={}
        n=len(inorder)
        for i,v in enumerate(inorder):
            dic[v]=i
        def solve(inorder_start,inorder_end,post_start,post_end):
            if inorder_start>inorder_end or post_start>post_end:
                return None
            root=TreeNode(postorder[post_end])
            root_index=dic[root.val]
            root_left=root_index-inorder_start
            root.left=solve(inorder_start,root_index-1,post_start,post_start+root_left-1)
            root.right=solve(root_index+1,inorder_end,post_start+root_left,post_end-1)
            return root
            
        return solve(0,n-1,0,n-1)
        