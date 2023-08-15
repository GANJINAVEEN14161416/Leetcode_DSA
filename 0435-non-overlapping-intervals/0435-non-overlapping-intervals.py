class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        n=len(intervals)
        ans=[intervals[0]]
        count=0
        for n1,n2 in intervals[1:]:
            if ans[-1][1]>n1:
                count+=1
            else:
                ans.append([n1,n2])
        return count
            
        