from collections import *
class Solution:
	def wordLadderLength(self,beginWord, endWord, wordList):
		#Code here
        if endWord not in wordList:
            return 0
        nei=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
        visit=set([beginWord])
        q=deque([beginWord])
        count=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return count
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            count+=1
        return 0
#{ 
 # Driver Code Starts
# from collections import deque 
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n = int(input())
		wordList = []
		for i in range(n):
			wordList.append(input().strip())
		startWord = input().strip()
		targetWord = input().strip()
		obj = Solution()
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends