

#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(firstHead,secondHead):
    l1,l2=0,0
    cur1=firstHead
    cur2=secondHead
    while cur1:
        l1+=1
        cur1=cur1.next
    while cur2:
        l2+=1
        cur2=cur2.next 
    if l1<l2:
        s3=l2-l1
        while s3>0:
            secondHead=secondHead.next 
            s3-=1
    else:
        s3=l1-l2
        while s3>0:
            firstHead=firstHead.next
            s3-=1
    while secondHead and firstHead:
        if secondHead==firstHead:
            return secondHead.data
        secondHead=secondHead.next
        firstHead=firstHead.next
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