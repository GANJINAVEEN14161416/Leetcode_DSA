class Solution:
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        arr.sort()
        n=len(arr)
        lis=[1]*(n)
        hash=[0]*n
        lastind=0
        mx=1
        for i in range(n):
            hash[i]=i
            for j in range(0,i):
                if (arr[i]%arr[j]==0)and lis[i]<1+lis[j]:
                    lis[i]=1+lis[j]
                    hash[i]=j
            if lis[i]>mx:
                mx=lis[i]
                lastind=i
        temp=[]
        while hash[lastind]!=lastind:
            temp.append(arr[lastind])
            lastind=hash[lastind]
        temp.append(arr[lastind])
        return temp[::-1]
        
        