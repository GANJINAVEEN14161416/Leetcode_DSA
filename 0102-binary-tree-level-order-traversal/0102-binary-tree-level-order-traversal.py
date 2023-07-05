# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        q=deque()
        ans=[]
        q.append(root)
        while q:
            list1=[]
            for i in range(len(q)):
                pop=q.popleft()
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
                list1.append(pop.val)
            if list1:
                ans.append(list1)
        return ans
            
        