class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        map1 = []
        map2 = []
        for value in nums1:
            if value not in nums2 and value not in map1:
                map1.append(value)
        for value in nums2:
            if value not in nums1 and value not in map2:
                map2.append(value)

        return [map1, map2]
    
class Solution2:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]

