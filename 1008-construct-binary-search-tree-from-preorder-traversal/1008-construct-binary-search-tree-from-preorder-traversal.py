# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def BST(preorder,i,bound):
            if i[0]==len(preorder) or preorder[i[0]]>bound:
                return 
            root=TreeNode(preorder[i[0]])
            i[0]+=1
            root.left=BST(preorder,i,root.val)
            root.right=BST(preorder,i,bound)
            return root
        i=[0]
        return BST(preorder,i,float('inf'))
        