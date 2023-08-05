
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        dummy=ListNode(-1)
        dup=dummy
        while cur and cur.next:
            dup.next=ListNode(cur.val)
            dup=dup.next
            value=gcd(cur.val,cur.next.val)
            dup.next=ListNode(value)
            dup=dup.next
            cur=cur.next
        dup.next=ListNode(cur.val)
        return dummy.next
        