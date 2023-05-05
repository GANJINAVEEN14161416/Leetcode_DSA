class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
            def dfs(row,col,sr,sc,color,sourse,image):
                if sr<0 or sr>=row or sc<0 or sc>=col:
                    return 
                if sourse!=image[sr][sc]:
                    return 
                else:
                    image[sr][sc]=color
                    dfs(row,col,sr-1,sc,color,sourse,image)
                    dfs(row,col,sr+1,sc,color,sourse,image)
                    dfs(row,col,sr,sc-1,color,sourse,image)
                    dfs(row,col,sr,sc+1,color,sourse,image)
            if image[sr][sc]==color:
                return image
            else:
                dfs(len(image),len(image[0]),sr,sc,color,image[sr][sc],image)
                return image
            


        
        