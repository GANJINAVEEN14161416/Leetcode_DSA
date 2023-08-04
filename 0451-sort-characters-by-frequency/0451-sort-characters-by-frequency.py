class Solution:
    def frequencySort(self, s: str) -> str:
        m=Counter(s)
        s1=dict(sorted(m.items(),key=lambda x:x[1],reverse=True))
        string=""
        for i,j in s1.items():
            string+=i*j
        return string


