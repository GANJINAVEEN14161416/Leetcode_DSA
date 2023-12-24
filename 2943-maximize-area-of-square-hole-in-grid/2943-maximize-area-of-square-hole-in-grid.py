class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        hBars.sort()
        vBars.sort()

        def max_con(nums):
            count=1
            max_con_hor=1
            for i in range(len(nums)-1):
                if nums[i]+1==nums[i+1]:
                    count+=1
                else:
                    count=1
                max_con_hor=max(max_con_hor,count)
            return max_con_hor
        max_con_hor=max_con(hBars)
        max_con_ver=max_con(vBars)
        min_side=min(max_con_hor,max_con_ver)
        return (min_side+1)**2
        
        
        
                
            