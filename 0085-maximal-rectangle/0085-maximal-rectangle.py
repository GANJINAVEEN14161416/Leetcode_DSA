class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n,m=len(matrix),len(matrix[0])
        heights=[0]*(m)
        maxarea=0
        for r in matrix:
            for i in range(m):
                if r[i]=="1":
                    heights[i]+=1
                else:
                    heights[i]=0
            stack=[]
            for i,v in enumerate(heights):
                start=i
                while stack and stack[-1][1]>v:
                    index,height=stack.pop()
                    maxarea=max(maxarea,(i-index)*height)
                    start=index
                stack.append((start,v))
            for i,h in stack:
                maxarea=max(maxarea,h*(len(heights)-i))
        return maxarea

