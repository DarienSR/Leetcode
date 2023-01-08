"""
  Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
  An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(str):
  stack = []
  if(len(str) == 1): return False # if the string has one character it is obviously invalid, no closing character
  for val in str: 
    if(val == '(' or val == '{' or val == '['): # push the open characters onto the stack
      stack.append(val)
    # since it isn't an open character, we have encountered a closing character. Before popping off the stack, check to see if ordering is valid 
    elif ((len(stack) <= 0) or (stack[len(stack) - 1] == '(' and val != ')') or (stack[len(stack) - 1] == '{' and val != '}') or (stack[len(stack) - 1] == '[' and val != ']')):
        return False # ordering invalid
    else:
      stack.pop() # ordering is valid, so remove it from the stack
  if(len(stack) != 0): return False # should have nothing remaining on the stack
  return True 
print(isValid("(("))
print(isValid("(([)])"))
print(isValid("){"))

