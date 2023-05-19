'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    def tour(self,lis, n):
        fuel = 0
        deficit = 0
        start = 0
        for i in range(n):
            fuel += lis[i][0] - lis[i][1]
            if fuel < 0:
                deficit += fuel
                fuel = 0
                start = i + 1
        return start%n if fuel + deficit >= 0 else -1
            


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends