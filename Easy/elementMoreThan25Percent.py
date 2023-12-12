class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        map = {}
        for value in arr:
            map[value] = map[value] + 1 if value in map else 1
        return max(map, key=map.get)