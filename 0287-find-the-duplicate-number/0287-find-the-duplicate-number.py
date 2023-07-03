class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        temp=0
        while True:
            slow=nums[slow]
            temp=nums[temp]
            if temp==slow:
                return slow
            
        