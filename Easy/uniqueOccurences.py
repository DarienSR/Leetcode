"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for index, value in enumerate(arr):
            map[value] = map[value] + 1 if (value in map) else 1

        temp = []
        for value in map:
            if map[value] in temp: return False
            temp.append(map[value])
        return True
