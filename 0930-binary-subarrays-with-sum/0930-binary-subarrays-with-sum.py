class Solution:
    def numSubarraysWithSum(self, nums: List[int], S: int) -> int:
        c = collections.Counter({0: 1})
        psum = res = 0
        for i in nums:
            psum += i
            res += c[psum - S]
            c[psum] += 1
        return res
            