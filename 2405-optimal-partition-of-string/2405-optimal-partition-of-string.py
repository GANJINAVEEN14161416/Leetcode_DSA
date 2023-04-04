class Solution:
    def partitionString(self, s: str) -> int:
        partition=set()
        count=0
        for n in s:
            if n in partition:
                count+=1
                partition=set()
                partition.add(n)
            else:
                partition.add(n)
        return count+1