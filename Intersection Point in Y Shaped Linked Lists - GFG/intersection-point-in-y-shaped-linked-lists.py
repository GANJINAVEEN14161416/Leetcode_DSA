

#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    p1=head1
    p2=head2
    l1,l2=0,0
    while p1:
        l1+=1
        p1=p1.next
    while p2:
        l2+=1
        p2=p2.next
    if l1>l2:
        diff=l1-l2
        while head1 and diff>0:
            head1=head1.next
            diff-=1
    elif l1<l2:
        diff=l2-l1
        while head2 and diff>0:
            head2=head2.next
            diff-=1
    while head1 and head2:
        if head1==head2:
            return head1.data
        head1=head1.next
        head2=head2.next
    return -1
        
# def intersetPoint(head1,head2):
#     h1=head1
#     h2=head2
#     m=dict()
#     while (h1!=None):
#         m[h1]='visited'
#         h1=h1.next
#     while (h2!=None):
#         if h2 in m.keys():
#             return h2.data
#         h2=h2.next
#     return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        temp=None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        x,y,z = map(int,input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))

        for x in nodes_a:
            node=Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node=Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node=Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i== 0:
                b.append(node)  # add to the end of the list b, only the intersection
        
        print(intersetPoint(a.head,b.head))

# } Driver Code Ends