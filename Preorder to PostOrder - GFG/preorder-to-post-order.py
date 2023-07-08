#User function Template for python3

class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def post_order(preorder, size) -> Node:
    def BST(preorder,i,bound):
        if i[0]==len(preorder) or preorder[i[0]]>bound:
            return 
        root=Node(preorder[i[0]])
        i[0]+=1
        root.left=BST(preorder,i,root.data)
        root.right=BST(preorder,i,bound)
        return root
    i=[0]
    return BST(preorder,i,float('inf'))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data,end=' ')

if __name__ == '__main__':
    t=int(input())

    for _tcs in range(t):
        size=int(input())
        pre=[int(x)for x in input().split()]

        root=post_order(pre,size)

        postOrd(root)
        print()
# } Driver Code Ends