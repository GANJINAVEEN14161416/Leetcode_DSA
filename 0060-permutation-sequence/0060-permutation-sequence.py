class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact=1
        number=[]
        for i in range(1,n):
            fact*=i
            number.append(i)
        number.append(n)
        k-=1
        ans=""
        while True:
            ans+=str(number[k//fact])
            number.pop(k//fact)
            if len(number)==0:
                break
            k=k%fact
            fact=fact//len(number)
        return ans
        