class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxm=0
        p=0
        mnm=float('inf')
        for i in range(len(prices)):
            if prices[i]<mnm:
                mnm=prices[i]
            p=prices[i]-mnm
            if p>mxm:
                mxm=p
        return mxm
            
        