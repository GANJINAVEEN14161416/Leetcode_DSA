from collections import *
class Solution:
	def wordLadderLength(self, beginWord, endWord, wordList):
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