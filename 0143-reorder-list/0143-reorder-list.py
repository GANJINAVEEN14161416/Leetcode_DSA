# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        prev=slow.next=None
        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt
        first,last=head,prev
        while last:
            nxt1,nxt2=first.next,last.next
            first.next=last
            last.next=nxt1
            first,last=nxt1,nxt2
        
        