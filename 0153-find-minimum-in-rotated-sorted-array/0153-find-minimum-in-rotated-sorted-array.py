class Solution:
    def findMin(self, arr: List[int]) -> int:
        n=len(arr)
        left=0
        right=n-1
        ans=1e9
        while left<=right:
            mid=(left+right)//2
            if arr[left]<=arr[mid]:
                ans=min(ans,arr[left])
                left=mid+1
            else:
                ans=min(ans,arr[mid])
                right=mid-1
        return ans    