class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count=0
        visit=set()
        def bfs(grid,r,c):
            q=deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row,col=q.popleft()
                direction=[[0,1],[1,0],[-1,0],[0,-1]]
                for dr,dc in direction:
                     r,c=dr+row,dc+col
                     if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c]=="1" and (r,c) not in visit:
                            visit.add((r,c))
                            q.append((r,c))

                            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1" and (r,c) not in visit:
                    count+=1
                    bfs(grid,r,c)
        return count