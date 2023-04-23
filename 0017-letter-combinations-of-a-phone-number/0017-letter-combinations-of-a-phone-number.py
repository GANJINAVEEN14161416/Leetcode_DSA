class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        chars=[]
        for c in digits:
            chars.append(dic[c])
        code=product(*chars)
        if digits=="":# edge case
            return []
        list1=[]
        for k in code:
            list1.append(''.join(k))
        return list1
