class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        space = [0,0,0]

        for n in nums:
            space[n]+=1
        print(space)
        m=0
        for i in range(len(space)):
            for j in range(space[i]):
                nums[m]=i
                m+=1
        return nums
        