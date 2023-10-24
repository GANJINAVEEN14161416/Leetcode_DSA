class Solution:
    def frequencySort(self, s: str) -> str:
        dic=defaultdict(int)
        ans=""
        for i in s:
            dic[i]+=1
        d=sorted(dic.items(),key=lambda x:-x[1])
        for i,v in d:
            ans+=i*v
        return ans
        