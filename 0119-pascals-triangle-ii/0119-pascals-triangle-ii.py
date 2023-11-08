class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[]
        def comb(r,c):
            val=1
            for i in range(c):
                val=val*(r-i)
                val=val//(i+1)
            return val
        for k in range(1,rowIndex+2):
            ans.append(comb(rowIndex,k-1))
        return ans
        
        
        