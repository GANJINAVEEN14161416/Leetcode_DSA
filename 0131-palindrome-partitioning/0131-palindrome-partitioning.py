class Solution:
    def partition(self, S: str) -> List[List[str]]:
        n=len(S)
        ans=[]
        def solve(start,path):
            if start==n:
                ans.append(path)
                return 
            for i in range(start,n):
                if S[start:i+1]==S[start:i+1][::-1]:
                    solve(i+1,path+[S[start:i+1]])
        solve(0,[])
        return ans
        