class Solution:
    def solveSudoku(self, grid: List[List[str]]) -> None:
        return self.solve(grid)
    def solve(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==".":
                    for c in range(1,len(grid)+1):
                        c=str(c)
                        if self.isvalid(i,j,c,grid):
                            grid[i][j]=c
                            if self.solve(grid)==True:
                                return True
                            else:
                                grid[i][j]="."
                    return False
        return True
    def isvalid(self,row,col,c,grid):
        for i in range(len(grid)):
            if grid[row][i]==c:
                return False
            if grid[i][col]==c:
                return False
            if grid[(3*(row//3)+i//3)][3*(col//3)+i%3]==c:
                return False
        return True

                            