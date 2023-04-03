class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        list1=[]
        potions.sort()
        # some test cases are not sorted
        for s in spells:
            #binary search on left most value i.e greater than success
            left,right,index=0,len(potions)-1,len(potions)# index is len(potions) in worst case where no values matches with potions values
            while left<=right:
                mid=(left+right)//2
                if s*potions[mid]>=success:
                    right=mid-1
                    index=mid
                else:
                    left=mid+1
            # add all possible values by total length -index
            list1.append(len(potions)-index)
        return list1
        