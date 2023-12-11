"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for value in nums:
            if value not in map:
                map[value] = 1
            else: return True
        return False
        