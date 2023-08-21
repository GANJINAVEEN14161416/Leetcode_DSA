class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,maxf=0,0
        dic=defaultdict(int)
        for right in range(len(s)):
            dic[s[right]]+=1
            maxf=max(maxf,dic[s[right]])
            if (right-left+1)-maxf>k:
                dic[s[left]]-=1
                left+=1
        return len(s)-left
