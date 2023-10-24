class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        mini=-1
        def solve(ind,temp,ans):
            if ind>=n:
                ans.append(temp)
                return
            for i in range(ind,n):
                if s[ind:i+1]==s[ind:i+1][::-1]:
                    solve(i+1,temp+[s[ind:i+1]],ans)
        solve(0,[],ans)
        return ans
        