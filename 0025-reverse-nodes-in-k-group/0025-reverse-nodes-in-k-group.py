# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev(head):
            prev=None
            while head:
                nxt=head.next
                head.next=prev
                prev=head
                head=nxt
            return prev
        def getListAfterReverseOperation(head, b):
            prevNode=None
            temp=head
            def findKthNode(temp,b):
                cur=temp
                while b>1 and cur:
                    cur=cur.next 
                    b-=1 
                return cur
            while temp:
                kthNode=findKthNode(temp,b)
                if kthNode==None:
                    if(prevNode):
                        prevNode.next=temp
                    break
                else:
                    nextNode=kthNode.next 
                    kthNode.next=None
                    dummy=rev(temp)
                    if temp==head:
                        head=dummy
                    else:
                        prevNode.next=kthNode
                    prevNode=temp 
                    temp=nextNode
            return head
        return getListAfterReverseOperation(head,k)
