class Solution:
    def reverseBits(self, n: int) -> int:
        answer=0
        for i in range(32):
            answer=answer | (n&1)<<(31-i)
            n=n>>1
        return answer
        