"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_num = 0
        for index, value in enumerate(nums):
            if value != 0:
                nums[next_num], nums[index] = nums[index], nums[next_num]
                next_num += 1


print(Solution.moveZeroes([4,2,4,0,0,3,0,5,1,0]))
