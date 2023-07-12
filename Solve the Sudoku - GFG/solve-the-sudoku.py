#User function Template for python3

class Solution:
    
    def SolveSudoku(self,sudoku):
        for i in range(len(grid)):
            for j in range(len(sudoku[0])):
                if sudoku[i][j]==0:
                    for k in range(1,10,1):
                        if self.isValid(i,j,k,sudoku):
                            sudoku[i][j]=k
                            
                            if self.SolveSudoku(sudoku)==True:
                                return True
                            else:
                               sudoku[i][j]=0
                    return False
                
        return True
    
    def isValid(self,row,col,k,sudoku):
        for i in range(len(sudoku)):
            
            if sudoku[row][i]==k:
                return False
            
            if sudoku[i][col]==k:
                return False
            
            if sudoku[3*(row//3)+i//3][3*(col//3)+i%3]==k:
                return False
        
        return True
        
            
        
        
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(grid[i][j],end=' ')
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends