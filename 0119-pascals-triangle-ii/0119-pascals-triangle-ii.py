class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[]
        def pascal(r,c):
            x=1
            for i in range(c):
                x=x*(r-i)//(i+1)
            return x

        for i in range(rowIndex+1):
            ans.append(pascal(rowIndex,i))
        return ans
                
                