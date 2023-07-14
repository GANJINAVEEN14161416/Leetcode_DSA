class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=deque()
        visit=set(wordList)
        if beginWord in visit:
            visit.remove(beginWord)
        q.append([beginWord,1])
        while q:
            word,steps=q.popleft()
            if endWord==word:
                return steps
            for i in range(len(word)):
                for j in range(97,123):
                    y=chr(j)
                    dup =word[:i]+y+word[i+1:]
                    if dup in visit:
                        q.append([dup,steps+1])
                        visit.remove(dup)
        return 0
        