class Solution:
    def countAndSay(self, n: int) -> str:
        stack=["1"]
        for i in range(n):
            current=stack[-1][0]
            count=1
            ans=""
            for k in stack[-1][1:]:
                if k==current:
                    count+=1
                else:
                    ans+=str(count)+current
                    current=k
                    count=1
            ans+=str(count)+current
            stack.append(ans)
        return stack[n-1]
        