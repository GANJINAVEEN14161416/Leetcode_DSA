class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        n=len(arr)
        ans=0
        index=-1
        if n==1:
            return 0

        left,right=1,n-2
        while left<=right:
            mid=(left+right)//2
            if arr[mid-1]<=arr[mid]>=arr[mid+1]:
                return mid
            elif arr[mid-1]<=arr[mid] and arr[mid]<=arr[mid+1]:
                left=mid+1
            else:
                right=mid-1
        if arr[0]>arr[n-1]:
            return 0
        else:
            return n-1
                
        