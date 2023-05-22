# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur=head
        for _ in range(k):
            if not cur:
                return head
            cur=cur.next
        prev=None
        cur=head
        if not cur:
            return prev
        x=k
        while x>0 and cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
            x-=1
        head.next=self.reverseKGroup(cur,k)
        return prev
        