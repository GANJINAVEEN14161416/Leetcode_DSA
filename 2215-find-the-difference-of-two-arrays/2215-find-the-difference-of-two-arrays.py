class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1=set(nums1)-set(nums2)
        list2=set(nums2)-set(nums1)
        return [list1,list2]