class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        stack=[intervals[0]]
        for i in range(1,len(intervals)):
            x=intervals[i][0]
            y=intervals[i][1]
            if stack[-1][1]>=x:
                stack[-1][1]=max(y,stack[-1][1])
            else:
                stack.append([x,y])
        return stack
            
        
        