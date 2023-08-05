class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        count=0
        while purchaseAmount>=5:
            count+=1
            purchaseAmount-=10
        return 100-(10*count)
        