class Solution:
    def parseBoolExpr(self, S: str) -> bool:
    
        def parseBoolExpr(S, t=True, f=False):
            return eval(S.replace('!', 'not |').replace('&(', 'all([').replace('|(', 'any([').replace(')', '])'))
        return parseBoolExpr(S,t=True,f=False)
        


        