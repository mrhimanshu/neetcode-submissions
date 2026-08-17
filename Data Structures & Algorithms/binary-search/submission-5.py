class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
    
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1

        while low<=high:
            median = low + (high-low)//2
            if nums[median]==target:
                return median
            elif nums[median]<target:
                low = median + 1
            else:
                high = median - 1
        return -1

        