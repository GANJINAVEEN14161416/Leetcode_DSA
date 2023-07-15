class Solution:
    def compress(self, chars: List[str]) -> int:
        n,k,left=len(chars),0,0
        while left<n:
            right=left
            while right<n and chars[left]==chars[right]:
                right+=1
            chars[k]=chars[left]
            k+=1
            if (right-left)>1:
                for c in str(right-left):
                    chars[k]=c
                    k+=1
            left=right
        return k
        