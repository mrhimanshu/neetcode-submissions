# Max Consecutive Ones

# Easy
# Topics
# Company Tags
# You are given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:
# Input: nums = [1,1,0,1,1,1]

# Output: 3

# Example 2:
# Input: nums = [1,0,1,1,0,1]

# Output: 2
# Constraints:
# 1 <= nums.length <= 100,000
# nums[i] is either 0 or 1.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=0
        b=0
        for n in nums:
            if n==1:
                b+=1
                if b>a:
                    a=b
            if n==0:
                b=0
        return a