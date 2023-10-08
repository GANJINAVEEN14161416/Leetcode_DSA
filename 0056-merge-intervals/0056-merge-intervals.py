class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack=[intervals[0]]
        for i,j in intervals[1:]:
            if i<=stack[-1][1]:
                stack[-1][1]=max(j,stack[-1][1])
            else:
                stack.append([i,j])
        return stack
                