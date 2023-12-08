"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    seeker = 0 
    for value in t:
        if seeker + 1 > len(s): return True # WE HAVE RAN THROUGH ALL VALUES IN S WHICH HAVE BEEN CONFIRMED TO BE SUBSEQUENT. WE DO NOT NEED TO CONTINUE WITH T
        if value == s[seeker]: seeker += 1
    if seeker == len(s): return True
    return False