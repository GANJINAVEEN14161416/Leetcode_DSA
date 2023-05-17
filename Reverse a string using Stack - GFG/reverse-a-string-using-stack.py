#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(s):
    stack=[]
    ans=""
    for i in s:
        stack.append(i)
    for i in range(len(stack)):
        ans+=stack.pop()
    return ans
        
    
    
    
    
    
    #Add code here

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends