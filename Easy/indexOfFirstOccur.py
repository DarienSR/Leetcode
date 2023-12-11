class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pointer = 0
        i = 0 # define here cause you cannot overwrite index i in for loop
        while(i < len(haystack)):
            if haystack[i] == needle[pointer]: pointer += 1 # move along string to verify match
            else: # value does not match we must restart. Move anchor up one and restart
                i = i - pointer # anchor moved up to next letter 
                pointer = 0 # restart pointer to look at first letter in new window position
            
            if pointer == len(needle): # we have a match
                return (i - len(needle)) + 1
            i += 1 
        return -1