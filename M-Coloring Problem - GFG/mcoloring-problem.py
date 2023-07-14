#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    color = [0]*V
    def isPossibleCol(node,col,graph,V):
        for i in range(V):
            if graph[node][i]==1 and color[i]==col:
                return False
        return True
    def solve(graph,node,V):
        if node == V:
            return True
        for col in range(1,k+1):
            if isPossibleCol(node,col,graph,V):
                color[node] = col
                if solve(graph,node+1,V) == True:
                    return True
                color[node] = 0
        return False
    return solve(graph,0,V)
    
    #your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends