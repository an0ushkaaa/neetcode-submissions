class Solution:
    def arrangeCoins(self, n: int) -> int:
        stair=0
        m=1
        while n>0:
            stair+=1
            m+=1
            n-=1*m
        return stair
