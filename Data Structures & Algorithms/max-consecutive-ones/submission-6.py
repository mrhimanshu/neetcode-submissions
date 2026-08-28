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