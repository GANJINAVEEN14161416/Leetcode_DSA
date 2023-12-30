
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def rowpascal(rowIndex):
            ans=[]
            def pascal(r,c):
                x=1
                for i in range(c):
                    x=x*(r-i)//(i+1)
                return x

            for i in range(rowIndex+1):
                ans.append(pascal(rowIndex,i))
            return ans
        ans=[]
        for i in range(numRows):
            ans.append(rowpascal(i))
        return ans
        
        
            