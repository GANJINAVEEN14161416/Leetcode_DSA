class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        for i in nums:
            if k>=i:
                k+=1
            else:
                break
        return k
        