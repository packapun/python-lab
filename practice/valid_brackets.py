"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


"""
input : string '{}'
output: true/false

Simple solution: 
If there was only one type of bracket {}, use a counter {{{}}}, }

Case 1: {{}} Perfectly balanced, counter == 0 
Case 2: } Opening bracket is abset counter = -1 which is invalid 
Case 3: {{{} Closing/opening brackets are missing which means that the input is not balanced


3 different types : 
(', ')', '{', '}', '[' and ']', 
6 entries that we need to check 
Simple stack? 

{()}

{ push
( push
) pop
} pop
check if stack is empty

O(len(s))

"""

def isValidBracketSeq(s:str) -> bool :
    mapping = {']':'[',')':'(', '}':'{'}
    stack = []
    for char in s: 
        if char in mapping:
            # Closing bracket   
            expected_bracket = mapping[char]
            if not stack or stack[-1] != expected_bracket:
                return False
            stack.pop()
        else:
            # Opening bracket
            stack.append(char)
    return len(stack) == 0
# O(len(s)) time O(k) space where k is the number of different brackets 

# test 
input = "[[[[]]]]"
print(isValidBracketSeq(input))