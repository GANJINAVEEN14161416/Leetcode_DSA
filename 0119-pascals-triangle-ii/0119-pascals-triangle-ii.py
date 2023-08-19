class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def value(numRows,col):
            ans=1
            for i in range(col):
                ans=ans*(numRows-i)
                ans=ans//(i+1)
            return ans
        res=[]
        for k in range(1,rowIndex+2):
            res.append(value(rowIndex,k-1))
        return res
            
            
            
