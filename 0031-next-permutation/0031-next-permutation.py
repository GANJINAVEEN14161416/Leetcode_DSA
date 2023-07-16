class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(arr)
        index=-1
        for i in range(n-1,0,-1):
            if arr[i]>arr[i-1]:
                index=i-1
                break
        if index==-1:
            return arr.sort()
        for i in range(n-1,0,-1):
            if arr[i]>arr[index]:
                arr[index],arr[i]=arr[i],arr[index]
                break
        r=n-1
        l=index+1
        while l<=r:
            arr[l],arr[r]=arr[r],arr[l]
            r-=1
            l+=1
        