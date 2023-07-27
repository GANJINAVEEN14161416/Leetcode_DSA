class Solution(object):
    def largestIsland(self, grid : List[List[int]]) -> int:
        #  creating the DSU functions inside the Solution class
        def findParent(node):
            if parent[node] != node:
                parent[node] = findParent(parent[node])
            return parent[node]
        def unionSize(u,v):
            pu = findParent(u)
            pv = findParent(v)
            if pu == pv:
                return 
            if size[pu]<size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]
        n = len(grid)
        parent = [i for i in range(n*n)]
        size = [1 for i in range(n*n)]
        #  step 1 connecting the components and finding their size
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                delRow = [-1,0,1,0]
                delCol = [0,-1,0,1]
                for i in range(4):
                    nr = row + delRow[i]
                    nc = col + delCol[i]
                    if nr>=0 and nr<n and nc>=0 and nc<n and grid[nr][nc] == 1:
                        NodeNo,adjNodeNo = (row*n)+col , (nr*n)+nc
                        unionSize(NodeNo,adjNodeNo)
        
        #  step2 Convert all 0 to 1
        mx = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue
                delRow = [-1,0,1,0]
                delCol = [0,1,0,-1]
                comp = set()
                for i in range(4):
                    nr = row + delRow[i]
                    nc = col + delCol[i]
                    if nr>=0 and nr<n and nc>=0 and nc<n and grid[nr][nc]==1:
                        a = nr*n + nc
                        comp.add(findParent(a)) 

                sizeTotal = 0
                for it in comp:
                    sizeTotal += size[it]
                mx = max(mx,sizeTotal + 1)
        for cellNo in range(n*n):
            mx = max(mx,size[findParent(cellNo)])
        return mx
        