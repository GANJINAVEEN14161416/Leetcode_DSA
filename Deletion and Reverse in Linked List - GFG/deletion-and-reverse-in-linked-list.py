
# Function to delete a given node from the list 
def deleteNode(head, key):
    #your code goes here
    dummy=Node(-1)
    cur=head
    while cur.next!=head:
        if cur.next.data==key:
            cur.next=cur.next.next
        else:
            cur=cur.next
    return head
def reverse(head):
    cur=head
    prev=None
    temp=cur.next
    cur.next=prev
    prev=cur
    cur=temp
    while cur!=head:
        temp=cur.next
        cur.next=prev
        prev=cur
        cur=temp
    head.next=prev
    head=prev
    cur=head
    while cur.next!=head:
        cur.data,cur.next.data=cur.next.data,cur.data
        cur=cur.next
    return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def push(data, prev):
    if prev == None:
        prev = Node(data)
        return prev
    tmp = Node(data)
    prev.next = tmp
    return tmp

def printList(head):
    flg = False
    tmp = head
    while flg== False or tmp!=head:
        flg = True
        print(tmp.data, end=" ")
        tmp = tmp.next
    print()

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]
        delNode = int(input())

        head = Node(None)
        prev = head
        for i in arr:
            prev = push(i, prev)
        head = head.next
        prev.next = head
        deleteNode(head, delNode)
        reverse(head)
        printList(head)

# } Driver Code Ends