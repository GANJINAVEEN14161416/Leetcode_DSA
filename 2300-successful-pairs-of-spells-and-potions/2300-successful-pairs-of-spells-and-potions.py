class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        list1=[]
        potions.sort()
        for s in spells:
            left,right,index=0,len(potions)-1,len(potions)
            while left<=right:
                mid=(left+right)//2
                if s*potions[mid]>=success:
                    right=mid-1
                    index=mid
                else:
                    left=mid+1
            list1.append(len(potions)-index)
        return list1
        