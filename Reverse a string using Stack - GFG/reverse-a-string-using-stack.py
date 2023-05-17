#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(s):
    n=len(s)
    list1=[]
    answer=""
    for i in s:
        list1.append(i)
    for i in range(len(list1)):
        answer+=list1.pop()
    return answer


#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends