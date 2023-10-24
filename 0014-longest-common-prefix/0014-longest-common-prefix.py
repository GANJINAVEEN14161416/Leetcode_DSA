class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        small_word=strs[0]
        ans=""
        for i in range(len(small_word)):
            if small_word[i]==strs[-1][i]:
                    ans+=small_word[i]
            else:
                break
        return ans