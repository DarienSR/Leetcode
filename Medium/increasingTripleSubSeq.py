""""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf') # set values to infinite
        for num in nums:
            if num <= first: # loop through and set lowest value in order, will reset if it finds another lower value
                first = num
            elif num <= second: # loop through and set second lowest value in order, will reset if it finds another second lower value
                second = num
            else: return True # this is the third value that is larger than the previous two values set
        return False # there is no sequence where first < second < third (return true)