
class Solution:
    def isPalindrome(self, head):
        length=0
        slow=head
        fast=head.next
        while fast and fast.next:
            if slow==fast:
                break
            slow=slow.next
            fast=fast.next.next
        prev=None
        second=slow.next
        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt
        while head and prev:
            if head.data!=prev.data:
                return False
            head=head.next
            prev=prev.next
        return True
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if Solution().isPalindrome(a.head):
            print(1)
        else:
            print(0)
# } Driver Code Ends