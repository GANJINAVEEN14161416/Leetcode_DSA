# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        list1=defaultdict(list)
        q=deque()
        q.append([root,0,0])
        while q:
            node,level,parent=q.popleft()
            list1[node.val]=[level,parent]
            if node.left:
                q.append([node.left,level+1,node.val])
            if node.right:
                q.append([node.right,level+1,node.val])
        if list1[x][0]==list1[y][0] and list1[x][1]!=list1[y][1]:
            return True
        return False
    
    
    
            
        