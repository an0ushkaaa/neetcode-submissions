class Solution:
    def trap(self, height: List[int]) -> int:
        r=len(height)-1
        l=0
        rm=0
        lm=0
        w=0
        while l<r:
            if height[l]>=height[r]:
                if height[r]>rm:
                    rm=height[r]
                else:
                    w+=rm-height[r]
                r-=1
            else:
                if height[l]>lm:
                    lm=height[l]
                else:
                    w+=lm-height[l]
                l+=1
        return w

        