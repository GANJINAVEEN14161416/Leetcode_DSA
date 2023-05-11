class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        list1=[]
        def search(target):
            left,right=0,len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return left
        l=search(target)
        r=search(target+1)-1
        if l<=r:
            return [l,r]
        return [-1,-1]



















        list1=[]
        if nums.count(target):
            list1.append(nums.index(target))
            for i in range(len(nums)-1,-1,-1):
                if nums[i]==target:
                    list1.append(i)
                    break
        else:
            return [-1,-1]
        return list1


