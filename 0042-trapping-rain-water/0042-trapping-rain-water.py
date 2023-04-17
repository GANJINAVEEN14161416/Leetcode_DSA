class Solution:
    def trap(self, height: List[int]) -> int:
        count=0
        left,right=0,len(height)-1
        leftmax,rightmax=height[left],height[right]
        while left<right:
            if leftmax<rightmax:
                left+=1
                leftmax=max(leftmax,height[left])
                count+=leftmax-height[left]
            else:
                right-=1
                rightmax=max(rightmax,height[right])
                count+=rightmax-height[right]
        return count
        