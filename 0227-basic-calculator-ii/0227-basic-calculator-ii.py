class Solution:
    def calculate(self, s: str) -> int:
        inner, outer, result, opt = 0, 0, 0, '+'
        for i in range(len(s) + 1):
            if i < len(s):
                c = s[i]
            else:
                c = '+'

            if c == ' ': 
                continue
            if c.isdigit():
                inner = 10 * inner + int(c)
                continue

            if opt == '+':
                result += outer
                outer = inner
            elif opt == '-':
                result += outer
                outer = -inner
            elif opt == '*':
                outer = outer * inner
            elif opt == '/':
                outer = int(outer / inner)
            inner, opt = 0, c
        return result + outer