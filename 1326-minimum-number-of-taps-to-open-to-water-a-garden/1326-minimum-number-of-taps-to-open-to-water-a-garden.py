class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        jump=[0]*(n+1)
        for i in range(len(ranges)):
            left=max(0,i-ranges[i])
            right=min(n,ranges[i]+i)
            jump[left]=max(jump[left],right-left)
        print(jump)
        ans=start=end=0
        for i in range(len(jump)-1):
            start=max(start,i+jump[i])
            if start==i and jump[i]==0:
                return -1
            if end==i:
                end=start
                ans+=1
        return ans
        