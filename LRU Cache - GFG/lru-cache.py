#User function Template for python3

# design the class in the most optimal way

from collections import OrderedDict
class LRUCache:
    def __init__(self,cap):
        self.cap=cap
        self.d=OrderedDict() 
    def get(self, key):
        if self.d.get(key):
            val=self.d.get(key)
            self.d.move_to_end(key) 
            return val
        else:
            return -1
    def set(self, key, value):
        if self.d.get(key):
            self.d[key]=value
            self.d.move_to_end(key) 
        else:
            if len(self.d)==self.cap:
                self.d.popitem(last=False) 
            self.d[key]=value

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry=int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        
        lru=LRUCache(cap)
        
       
        i=0
        q=1
        while q<=qry:
            qtyp=a[i]
            
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
        print()
# } Driver Code Ends