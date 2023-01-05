# Given an integer x, return true if x is a palindrome and false otherwise.

def isPalindrome(x:int) -> bool:
  palindrome = str(x)
  i = 0
  j = len(palindrome) - 1
  for x in palindrome:
    if palindrome[i] == palindrome[j]:
      i = i + 1
      j = j - 1
    else:
      return False
  return True

print(isPalindrome(11))


