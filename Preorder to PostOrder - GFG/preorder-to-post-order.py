#User function Template for python3

class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def post_order(preorder, size) -> Node:
    list1=sorted(preorder)
    def buildTree(preorder,inorder):
        if not preorder or not inorder:
            return None
        root=Node(preorder[0])
        index=inorder.index(preorder[0])
        root.left=buildTree(preorder[1:index+1],inorder[:index])
        root.right=buildTree(preorder[index+1:],inorder[index+1:])
        return root
    return buildTree(preorder,list1)


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