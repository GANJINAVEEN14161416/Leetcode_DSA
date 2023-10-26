#User function Template for python3
from collections import *
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        graph=defaultdict(list)
        for i in range(N-1):
            first=alien_dict[i]
            second=alien_dict[i+1]
            n=len(first)
            m=len(second)
            for j in  range(min(n,m)):
                if first[j]!=second[j]:
                    graph[ord(first[j])-97].append(ord(second[j])-97)
                    break
        indegree=[0]*K
        for i in range(K):
            for j in graph[i]:
                indegree[j]+=1
        q=deque()
        for i in range(K):
            if indegree[i]==0:
                q.append(i)
        count=0
        ans=[]
        while q:
            pop=q.popleft()
            ans.append(pop)
            count+=1
            for child in graph[pop]:
                indegree[child]-=1
                if indegree[child]==0:
                    q.append(child)
        if count==ans:
            return ans
        res=[]
        for i in ans:
            res.append(chr(i+97))
        return res



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