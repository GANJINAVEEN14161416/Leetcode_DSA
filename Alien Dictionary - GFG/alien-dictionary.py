#User function Template for python3
from collections import *
class Solution:
    def findOrder(self,alien_dict, N, K):
        def helper(adj,V):
            indegree=[0]*V
            for i in range(V):
                for j in adj[i]:
                    indegree[j]+=1
            q=deque()
            ans=[]
            count=0
            for i in range(V):
                if indegree[i]==0:
                    q.append(i)
            while q:
                node=q.popleft()
                count+=1
                ans.append(node)
                for child in adj[node]:
                    indegree[child]-=1
                    if indegree[child]==0:
                        q.append(child)
            if count==V:
                return ans
            return []
        adj=defaultdict(list)
        for i in range(N-1):
            first=alien_dict[i]
            second=alien_dict[i+1]
            mi=min(len(first),len(second))
            for j in range(mi):
                if first[j]!=second[j]:
                    adj[ord(first[j])-ord("a")].append(ord(second[j])-ord("a"))
                    break
        ans=helper(adj,K)
        s1=""
        for i in ans:
            s1+=chr(i+ord("a"))
        return s1 if s1 else ""
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends