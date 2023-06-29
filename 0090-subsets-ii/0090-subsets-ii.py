class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for i in nums:
            for j in range(len(ans)):
                x=ans[j][:]
                x.append(i)
                x.sort()
                if x not in ans:
                    ans.append(x)
                else:
                    continue
        return ans
        