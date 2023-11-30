class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left,right=1,max(bloomDay)
        ans=1e9
        n=len(bloomDay)
        def possible(mid):
            temp=0
            bookay=0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=mid:
                    temp+=1
                else:
                    bookay+=temp//k
                    temp=0
            bookay+=temp//k
            #print(bookay)
            return bookay
        while left<=right:
            mid=(left+right)//2
            temp=possible(mid)
            if temp<ans and temp>=m:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        if m*k>n:
            return -1
        return ans
        