class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = len(nums)
        if a!=len(set(nums)):
            return True
        else:
            return False