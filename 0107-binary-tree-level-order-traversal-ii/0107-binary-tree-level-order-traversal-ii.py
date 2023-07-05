# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        list1=[]
        q=deque()
        q.append(root)
        while q:
            level=[]
            for i in range(len(q)):
                poping=q.popleft()
                if poping:
                    level.append(poping.val)
                    q.append(poping.left)
                    q.append(poping.right)
            if level:
                list1.append(level)
        return list1[::-1]