class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length=0
        longest=0
        if len(nums)==0:
            return 0
        n=set(nums)
        for i in n:
            if i-1 not in n:
                length=1
                current=i
                while current+1 in n:
                    length+=1
                    current+=1
            longest=max(longest,length)
        return longest