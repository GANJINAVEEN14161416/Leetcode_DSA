class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        peoples=sorted(people)
        left,right,count=0,len(peoples)-1,0
        while left<=right:
            if peoples[left]+peoples[right]<=limit:
                left+=1
                count+=1
            else:
                count+=1
            right-=1
        return count
        