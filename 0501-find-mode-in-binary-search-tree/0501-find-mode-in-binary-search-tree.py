# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        dic=defaultdict(int)
        q.append(root)
        while q:
            pop=q.popleft()
            dic[pop.val]+=1
            if pop.left:
                q.append(pop.left)
            if pop.right:
                q.append(pop.right)
        largest=max(dic.values())
        ans=[]
        for i,v in dic.items():
            if dic[i]==largest:
                ans.append(i)
        return ans
            
            
            
        
        