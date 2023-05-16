#User function Template for python3
import collections
class Solution:
    def Anagrams(self, words, n):
        dic=collections.defaultdict(list)
        for word in words:
            sorted_word="".join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word].append(word)
            else:
                dic[sorted_word].append(word)
        return dic.values()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends