class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        dic=collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                dic[pattern].append(word)
        q=deque([beginWord])
        visit=set([beginWord])
        count=1
        while q:
            for j in range(len(q)):
                x=q.popleft()
                if x==endWord:
                    return count
                for i in range(len(x)):
                    pattern=x[:i]+"*"+x[i+1:]
                    for word in dic[pattern]:
                        if word not in visit:
                            visit.add(word)
                            q.append(word)
            count+=1
        return 0
                    
        
        