"""
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
"""

class Solution:
  def toLowerCase(self, s: str) -> str:
    new = ""
    for index, letter in enumerate(s):
      new += letter.lower()
    return new