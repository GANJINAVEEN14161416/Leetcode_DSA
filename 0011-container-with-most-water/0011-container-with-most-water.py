class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right,answer=0,len(height)-1,0
        while left<=right:
            area=min(height[right],height[left])*(right-left)
            answer=max(answer,area)
            if height[right]>height[left]:
                left+=1
            else:
                right-=1
        return answer
        
        
        
        
        
        
        
        # list1=[]
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         list1.append(min(height[i],height[j])*(j-i))
        # return max(list1)
        