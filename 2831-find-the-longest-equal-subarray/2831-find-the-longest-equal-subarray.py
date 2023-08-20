class Solution:
    def longestEqualSubarray(self, A: List[int], k: int) -> int:
        maxf = i = 0
        count =defaultdict(int)
        for j in range(len(A)):
            count[A[j]] += 1
            maxf = max(maxf, count[A[j]])
            if j - i + 1 - maxf > k:
                count[A[i]] -= 1
                i += 1
        return maxf
        