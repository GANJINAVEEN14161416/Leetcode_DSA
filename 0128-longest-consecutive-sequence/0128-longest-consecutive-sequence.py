class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        arr.sort()
        count=ans=0
        if not arr:
            return 0
        for i in range(len(arr)-1):
            if (arr[i+1]-arr[i])==1:
                count+=1
            elif (arr[i+1]-arr[i])==0:
                pass
            else:
                count=0
            ans=max(count,ans)
        return ans+1
        