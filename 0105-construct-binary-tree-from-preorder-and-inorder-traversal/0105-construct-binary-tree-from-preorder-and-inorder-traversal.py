# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n=len(preorder)
        if len(inorder)!=len(preorder):
            return None
        dic={}
        for i in range(n):
            dic[inorder[i]]=i
        istart=0
        iend=len(inorder)-1
        pstart=0
        pend=len(preorder)-1
        def build(inorder,preorder,istart,iend,pstart,pend):
            if istart>iend or pstart>pend:
                return None
            root=TreeNode(preorder[pstart])
            isroot=dic[preorder[pstart]]
            numleft=isroot-istart
            root.left=build(inorder,preorder,istart,isroot-1,pstart+1,pstart+numleft)
            root.right=build(inorder,preorder,isroot+1,iend,pstart+numleft+1,pend)
            return root
        root=build(inorder,preorder,istart,iend,pstart,pend)
        return root