class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans=0
        left=0
        count=defaultdict(int)
        for right in range(len(answerKey)):
            count[answerKey[right]]+=1
            ans=max(ans,count[answerKey[right]])
            if right-left+1-ans>k:
                count[answerKey[left]]-=1
                left+=1
        return len(answerKey)-left
    
        