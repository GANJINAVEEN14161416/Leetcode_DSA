#User function Template for python3

'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def splitList(self, head, head1, head2):
        # cur1=head
        # cur2=head
        # start=head
        # n=1
        # while cur1:
        #     if start==cur1.next:
        #         break
        #     cur1=cur1.next
        #     n+=1
        
            
            
            
            
            
            
            
            
            
            
            
            
            

        end1=head

        N=1

        end=head

        start = head

        while  head:

            if head.next ==start:

                break

            head=head.next

            N+=1

        end=head

        for i in range(N//2+N%2-1):

            end1=end1.next

        head2=end1.next

        end.next=head2

        end1.next=start

        return start,head2



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