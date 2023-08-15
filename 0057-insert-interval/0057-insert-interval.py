class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans=[intervals[0]]
        for n1,n2 in intervals[1:]:
            if ans[-1][1]>=n1:
                ans[-1][1]=max(ans[-1][1],n2)
            else:
                ans.append([n1,n2])
        return ans
                
        