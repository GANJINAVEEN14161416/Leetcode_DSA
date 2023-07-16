# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        list1=[]
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            list1.append(root.val)
            inorder(root.right)
        inorder(root)
        list1.sort()
        def BST(root,start,end):
            if start>end:
                return
            mid=(start+end)//2
            root=TreeNode(list1[mid])
            root.left=BST(root.left,start,mid-1)
            root.right=BST(root.right,mid+1,end)
            return root
        return BST(root,0,len(list1)-1)
        return root

        
        