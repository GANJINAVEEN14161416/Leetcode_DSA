# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def rev(head):
            prev=None
            while head:
                nxt=head.next 
                head.next=prev 
                prev=head 
                head=nxt 
            return prev      
        if head==None or head.next==None:
            return True
        slow=head
        fast=head.next
        cur=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        NextNode=slow.next
        slow.next=None
        NextLL=rev(NextNode)
        while NextLL and cur:
            if NextLL.val!=cur.val:
                return False 
            cur=cur.next 
            NextLL=NextLL.next 
        return True














    
        
        
    
