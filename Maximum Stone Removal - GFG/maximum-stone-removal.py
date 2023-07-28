#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def maxRemove(self, adj, n):
        max_row = 0
        max_col = 0
        
        for i in adj:
            max_row = max(max_row,i[0])
            max_col = max(max_col,i[1])
        ds = disjoinset(max_row+max_col+2)
        s = {}
        for i in adj:
            row_node = i[0]
            col_node = i[1]+max_row+1
            ds.union(row_node,col_node)
            s[row_node] = 0
            s[col_node] = 0
        count = 0
        for i in s:
            if ds.parent[i]==i:
                count+=1
        return len(adj)-count
            
            
class disjoinset:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        
    def find(self,a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        
        return self.parent[a]
    
    def union(self,a,b):
        
        pa = self.find(a)
        pb = self.find(b)
        
        if pa == pb:
            return 
        
        if self.rank[pa]>self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa]+=self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb]+=self.rank[pa]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        adj = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        res = ob.maxRemove(adj, n)
        print(res)
# } Driver Code Ends