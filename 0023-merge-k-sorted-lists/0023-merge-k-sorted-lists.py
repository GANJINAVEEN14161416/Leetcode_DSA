# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, arr: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not arr:
            return 
        def merge(l1,l2):
            dummy=ListNode(-1)
            cur=dummy
            while l1 and l2:
                if l1.val<=l2.val:
                    cur.next=l1
                    cur=cur.next
                    l1=l1.next
                else:
                    cur.next=l2
                    cur=cur.next
                    l2=l2.next
            if l1:
                cur.next=l1
            if l2:
                cur.next=l2
            return dummy.next
        def mergesort(arr):
            while len(arr)>1:
                merged=[]
                for i in range(0,len(arr),2):
                    l1=arr[i]
                    l2=arr[i+1] if (i+1)<len(arr) else None
                    merged.append(merge(l1,l2))
                arr=merged
            return arr[0]
        return mergesort(arr)

