class Solution:
    def minOperations(self, nums: List[int]) -> int:
        next_element=0
        ans=0
        for current in nums:
            if current<=next_element:
                ans+=next_element-current+1
                next_element+=1
            else:
                next_element=current
        return ans
                