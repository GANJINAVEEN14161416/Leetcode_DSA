class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        seen=set()
        num=1
        while len(seen)<n:
            if target-num not in seen:# condition first_num+second_num!=target
                seen.add(num)         # second_nums!=target-first_num
            num+=1
        return sum(seen)
                
        