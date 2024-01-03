class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        q = deque()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    q.append((i, j))
        four = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        while q:
            x, y = q.popleft()
            for i in range(4):
                newrow = x + four[i][0]
                newcol = y + four[i][1]
                while newrow < n and newrow >= 0 and newcol < m and newcol >= 0:
                    matrix[newrow][newcol] = 0
                    newrow += four[i][0]
                    newcol += four[i][1]
        