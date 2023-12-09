"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for index, value in enumerate(flowerbed):
            if value == 0 and (index+1 == len(flowerbed) or flowerbed[index+1] == 0) and (flowerbed[index-1] == 0 or index == 0):
                flowerbed[index] = 1
                n -= 1
        if n <= 0: return True
        else: return False