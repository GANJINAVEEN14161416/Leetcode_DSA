class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
        count=1
        n=len(nums)
        for i in range(n+n):
            if dic[count]:
                count+=1
            else:
                return count
        # TC:O(N)+O(N)
        # SC:O(N)
        
        