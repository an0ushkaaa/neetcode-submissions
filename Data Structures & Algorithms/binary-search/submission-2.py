class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        mid=int((start+end)/2)
        while start<end:
            if target>nums[mid]:
                start=mid+1
                mid=int((start+end)/2)
            elif target<nums[mid]:
                end=mid-1
                mid=int((start+end)/2)
            elif target==nums[mid]:
                        return int(mid)
        if nums[start]==target:
            return start
        return -1

            
        