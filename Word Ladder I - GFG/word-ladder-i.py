from collections import *
class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
		if targetWord not in wordList:
		    return 0
		dic=defaultdict(list)
		for word in wordList:
		    for i in range(len(word)):
		        pattern=word[:i]+"*"+word[i+1:]
		        dic[pattern].append(word)
		visit=set([startWord])
		q=deque([startWord])
		count=1
		while q:
		    for i in range(len(q)):
		        word=q.popleft()
		        if word==targetWord:
		            return count
		        for j in range(len(word)):
		            pattern=word[:j]+"*"+word[j+1:]
		            for n in dic[pattern]:
		                if n not in visit:
		                    q.append(n)
		                    visit.add(n)
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