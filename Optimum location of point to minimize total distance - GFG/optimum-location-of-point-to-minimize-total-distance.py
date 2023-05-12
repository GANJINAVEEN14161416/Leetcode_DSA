from typing import List
import math
class Solution:
    def calculate_distance(self,line,n,points,x):
        if line[1]==0: y=float('inf')
        else: y=-1*(line[2]+(line[0]*x))/line[1]
        dis=0
        for point in points:
            dis+=math.sqrt((point[0]-x)**2+(point[1]-y)**2)
        return dis
    def findOptimumCost(self, line : List[int], n : int, points : List[List[int]]) -> float:
        l=-1000
        r=1000
        mid1=0
        mid2=0
        ap=0.001 # absolute precision
        while abs(r-l)>=ap:
            mid1=l+(r-l)/3 # 1st third 
            mid2=r-(r-l)/3 # last third
            fmid1=self.calculate_distance(line,n,points,mid1)
            fmid2=self.calculate_distance(line,n,points,mid2)
            if fmid1>fmid2: l=mid1
            elif fmid1<fmid2: r=mid2
            else:
                l=mid1
                r=mid2
        return self.calculate_distance(line,n,points,r)
#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        line=IntArray().Input(3)
        
        
        n = int(input())
        
        
        points=IntMatrix().Input(n, 2)
        
        obj = Solution()
        res = obj.findOptimumCost(line, n, points)
        
        print("{0:.2f}".format(res))
        

# } Driver Code Ends