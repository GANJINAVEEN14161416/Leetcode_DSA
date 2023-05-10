class Solution:
    def minimumSum(self, num: int) -> int:
        string=str(num)
        list1=[]
        for i in string:
            list1.append(int(i))
        list1.sort()
        s1=int(str(list1[0])+str(list1[2]))
        s2=int(str(list1[1])+str(list1[3]))
        return s1+s2
            
        
        