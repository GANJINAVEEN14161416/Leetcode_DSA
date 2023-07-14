class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q=deque()
        n=len(image)
        m=len(image[0])
        row=len(image)
        col=len(image[0])
        if image[sr][sc]==color:
            return image
        temp=image[sr][sc]
        image[sr][sc]=color
        q.append([sr,sc])
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        visit=[[False]*m for i in range(n)]
        while q:
            r,c=q.popleft()
            for new in range(4):
                newrow=m1[new]+r
                newcol=m2[new]+c
                if newrow>=0 and newcol>=0 and newrow<row and newcol<col and not visit[newrow][newcol] and image[newrow][newcol]==temp:
                    image[newrow][newcol]=color
                    visit[newrow][newcol]=True
                    q.append([newrow,newcol])
        return image
                
        