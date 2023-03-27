class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c=nums1+nums2
        b=sorted(c)
        while len(b)!=2 and len(b)!=1:
            b.remove(b[0])
            b.pop()
        if len(b)==1:
            return b[0]
        elif len(b)==2:
            avg=sum(b)/2
            return avg
