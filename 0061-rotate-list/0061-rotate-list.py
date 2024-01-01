# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        cur=head
        if not head:
            return head
        while cur:
            length+=1
            cur=cur.next 
        k=k%length
        stop=length-k
        cur=head
        if k==0 or k==length:
            return head
        while stop>1:
            cur=cur.next
            stop-=1
        lastNode=cur.next
        temp=lastNode
        cur.next=None
        while lastNode.next:
            lastNode=lastNode.next 
        lastNode.next=head
        return temp