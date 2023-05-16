class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans=""
        def dfs(word,i,j,board):
            if len(word)==0:
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
                return False
            temp=board[i][j]
            board[i][j]="#"
            ans=dfs(word[1:],i-1,j,board) or dfs(word[1:],i+1,j,board) or dfs(word[1:],i,j+1,board) or dfs(word[1:],i,j-1,board)
            board[i][j]=temp
            return ans
            
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(word,i,j,board):
                    return True
        return False
        