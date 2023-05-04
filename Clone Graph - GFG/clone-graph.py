#User function Template for python3

class Solution():
    def cloneGraph(self, node):
        return node



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from queue import Queue
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

def bfs(src):
    ans = []
    q = Queue()
    visit = set()
    q.put(src)
    visit.add(src)
    while not q.empty():
        u = q.get()
        ans.append(u)
        for i in u.neighbors:
            if i not in visit:
                visit.add(i)
                q.put(i)
    return ans

def checkedClone(prev, new1):
    prevAns = bfs(prev)
    newAns = bfs(new1)
    return prevAns == newAns
    
    
if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        v = [Node(i) for i in range(N)]
        for i in range(N):
            v[i].neighbors = [v[int(i)] for i in input().split()]
        ob = Solution()
        ans = ob.cloneGraph(v[0])
        # if ans == v[0]:
        #     print(0)
        print(int(checkedClone(v[0], ans)))
# } Driver Code Ends