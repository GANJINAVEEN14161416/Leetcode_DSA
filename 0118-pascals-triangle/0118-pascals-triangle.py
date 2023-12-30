
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(numRows):
            temp=[]
            for j in range(i):
                if i==0 or j==0:
                    temp.append(1)
                else:
                    temp.append(ans[-1][j-1]+ans[-1][j])
                    
            temp.append(1)
            ans.append(temp)
        return ans
        
        
            