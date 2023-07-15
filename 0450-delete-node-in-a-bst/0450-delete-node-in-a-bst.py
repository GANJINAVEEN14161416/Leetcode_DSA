# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find(root):
            if not root.right:
                return root
            return find(root.right)
        def helper(root):
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                store=root.right
                temp=find(root.left)
                temp.right=store
                return root.left
        
        if not root:
            return root
        dummy=root
        if root.val==key:
            return helper(root) 
        while root:
            if key<root.val:
                if root.left and root.left.val==key:
                    root.left=helper(root.left)
                else:
                    root=root.left
            else:
                if root.right and key==root.right.val:
                    root.right=helper(root.right)
                else:
                    root=root.right 
        return dummy
                    
        