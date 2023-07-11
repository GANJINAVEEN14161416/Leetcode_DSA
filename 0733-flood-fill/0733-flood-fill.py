class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        q=deque()
        q.append([sr,sc])
        temp=image[sr][sc]
        rowmatrix=[0,-1,0,1]
        colmatrix=[1,0,-1,0]
        visit=[[False]*len(image[0]) for i in range(len(image))]
        visit[sr][sc]=True
        image[sr][sc]=color
        while q:
            row,col=q.popleft()
            for i in range(4):
                newrow=row+rowmatrix[i]
                newcol=col+colmatrix[i]
                if newrow>=0 and newrow<len(image) and newcol>=0 and newcol<len(image[0]) and not visit[newrow][newcol] and image[newrow][newcol]==temp:
                    q.append([newrow,newcol])
                    image[newrow][newcol]=color
                    visit[newrow][newcol]=True
        return image
            
        