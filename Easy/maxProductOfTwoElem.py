"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pointer = 1
        anchor = 0
        sum = 0
        i = 0
        j = 0

        while(anchor < len(nums)):
            if pointer >= len(nums):
                anchor += 1
                pointer = anchor + 1

            if anchor == len(nums) - 1: 
                return sum

            if (nums[pointer] - 1) * (nums[anchor] - 1) > sum:
                sum = (nums[pointer] - 1) * (nums[anchor] - 1)
                i = pointer
                j = anchor
            pointer += 1
