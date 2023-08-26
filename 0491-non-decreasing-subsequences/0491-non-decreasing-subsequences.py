class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if len(path) > 1:
                res.append(path[:])
            used_nums = set()
            for i in range(start, N):
                if nums[i] not in used_nums:
                    if not path or path[-1] <= nums[i]:
                        used_nums.add(nums[i])
                        path.append(nums[i])
                        backtrack(i + 1)
                        path.pop()
        N = len(nums)
        res = []
        path = []
        backtrack(0)
        return res
        