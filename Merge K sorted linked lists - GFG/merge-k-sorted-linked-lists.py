
class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        def merge(l1,l2):
            dummy=Node(-1)
            cur=dummy
            while l1 and l2:
                if l1.data<=l2.data:
                    cur.next=l1
                    cur=cur.next
                    l1=l1.next
                else:
                    cur.next=l2
                    cur=cur.next
                    l2=l2.next
            if l1:
                cur.next=l1
            if l2:
                cur.next=l2
            return dummy.next
        def mergesort(arr):
            while len(arr)>1:
                merged=[]
                for i in range(0,len(arr),2):
                    l1=arr[i]
                    l2=arr[i+1] if (i+1)<len(arr) else None
                    merged.append(merge(l1,l2))
                arr=merged
            return arr[0]
        return mergesort(arr)
                
                
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            
            heads.append(newList.head)
        
        merged_list = Solution().mergeKLists(heads,n)
        printList(merged_list)

# } Driver Code Ends