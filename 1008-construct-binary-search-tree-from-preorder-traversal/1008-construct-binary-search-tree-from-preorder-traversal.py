# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        list1=sorted(preorder)
        def buildTree(preorder,inorder):
            if not preorder or not inorder:
                return None
            root=TreeNode(preorder[0])
            index=inorder.index(preorder[0])
            root.left=buildTree(preorder[1:index+1],inorder[:index])
            root.right=buildTree(preorder[index+1:],inorder[index+1:])
            return root
        return buildTree(preorder,list1)
        