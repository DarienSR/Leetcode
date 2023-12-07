
"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array"""


class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    counter = {}
    for value in nums:
      if value in counter: 
        counter[value] += 1
      else:
        counter[value] = 1
    return max(counter, key=counter.get)
  
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2