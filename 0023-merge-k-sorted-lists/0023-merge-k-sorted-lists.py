# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list1=[]
        linked1=linked2=ListNode(0)
        for i in lists:
            while i:
                list1.append(i)
                i=i.next
        list1.sort(key=lambda x:x.val)
        for i in list1:
            linked1.next=i
            linked1=linked1.next
        return linked2.next

