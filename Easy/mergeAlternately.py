"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        pointer = 0

        for value in word1:
            s += value
            if pointer < len(word2):
                s += word2[pointer]
                pointer += 1
        
        if pointer < len(word2):
            for value in word2[pointer:]:
                s += value
        return s