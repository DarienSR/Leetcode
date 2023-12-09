class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      m = max(candies)
      arr = []
      for value in candies:
          if value + extraCandies >= m: arr.append(True)
          else: arr.append(False)
      return arr