class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        intervals=[0]*(101)
        for l,r in clips:
            intervals[l]=max(intervals[l],r)
        hi=lo=res=0
        while hi < time:
            lo, hi = hi, max(intervals[lo:hi+1])
            if hi <= lo: return -1
            res += 1
        return res

        
        