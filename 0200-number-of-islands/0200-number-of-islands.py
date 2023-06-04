class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        def dfs(grid,row,col,r,c):
            if r<0 or r>=row or c>=col or c<0 or grid[r][c]!="1":
                return 
            grid[r][c]="2"
            dfs(grid,row,col,r-1,c)
            dfs(grid,row,col,r+1,c)
            dfs(grid,row,col,r,c-1)
            dfs(grid,row,col,r,c+1)
        
            
        
        
        
        count=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    count+=1
                    dfs(grid,len(grid),len(grid[0]),r,c)
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not grid:
#             return 0
#         def dfs(grid,row,col,r,c):
#             if r<0 or r>=row or c<0 or c>=col or grid[r][c]!="1":
#                 return
#             grid[r][c]="2"
#             dfs(grid,row,col,r-1,c)
#             dfs(grid,row,col,r+1,c)
#             dfs(grid,row,col,r,c-1)
#             dfs(grid,row,col,r,c+1)
#         count=0
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c]=="1":
#                     count+=1
#                     dfs(grid,len(grid),len(grid[0]),r,c)
#         return count

        
        
        