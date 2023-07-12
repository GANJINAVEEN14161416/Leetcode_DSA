class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=deque()
        # if endWord not in wordList:
        #     return 0
        visit=set(wordList)
        q.append([beginWord,1])
        if beginWord in visit:
            visit.remove(beginWord)
        while q:
            word,steps=q.popleft()
            if word==endWord:
                return steps
            for i in range(len(word)):
                for j in range(97,123):
                    y=chr(j)
                    dup=word[:i]+y+word[i+1:]
                    if dup in visit:
                        visit.remove(dup)
                        q.append([dup,steps+1])
        return 0
        