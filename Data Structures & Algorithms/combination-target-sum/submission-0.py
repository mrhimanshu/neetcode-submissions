class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, curr, total):
            # Base cases
            if total == target:
                res.append(curr[:])
                return
            if total > target:
                return
            
            # Recursive exploration
            for i in range(start, len(nums)):
                curr.append(nums[i])
                # since we can reuse the same number, we call backtrack(i, ...)
                backtrack(i, curr, total + nums[i])
                curr.pop()  # backtrack
        
        backtrack(0, [], 0)
        return res