class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        pointer = len(s) - 1 
        n = list(s)
        for index, value in enumerate(n):
            if index >= pointer: return "".join(n)
            if value in vowels:
                while n[pointer] not in vowels:
                    pointer -= 1
                n[index] = n[pointer]
                n[pointer] = value
                pointer -= 1
        return "".join(n)


          
