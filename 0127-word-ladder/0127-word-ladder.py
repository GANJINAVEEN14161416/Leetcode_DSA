class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        s=set(wordList)
        q=deque()
        q.append([beginWord,1])
        while q:
            word,count=q.popleft()
            if endWord==word:
                return count
            for i in range(len(word)):
                for j in range(97,123):
                    dup=word[:i]+chr(j)+word[i+1:]
                    if dup in s:
                        s.remove(dup)
                        q.append([dup,count+1])
        return 0