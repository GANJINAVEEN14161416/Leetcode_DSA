#User function Template for python3


class Solution:
    def splitList(self, head, head1, head2):
        #code here
        cur=head
        start=head
        n=1
        while cur:
            if cur.next==start:
                break
            cur=cur.next
            n+=1
        end=cur
        first=head
        half=n//2+n%2-1
        while half and first:
            first=first.next
            half-=1
        second=first.next
        first.next=head
        end.next=second
        return head,second






#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:
    def __init__(self):
        self.data = None
        self.next = None

def printCircularLinkedList(head):
    tmp = head
    while True:
        print(tmp.data, end = " ")
        tmp = tmp.next
        if tmp == head:
            break
    print()
    
if __name__ == "__main__":
    for i in range(int(input())):
        head = Node()
        head1 = Node()
        head2 = Node()
        tmp = head
        n = int(input())
        for i in input().split():
            tmp.next = Node()
            tmp = tmp.next
            tmp.data = int(i)
        head = head.next
        tmp.next = head
        obj = Solution()
        head1,head2 = obj.splitList(head,head1,head2)
        printCircularLinkedList(head1)
        printCircularLinkedList(head2)


# } Driver Code Ends