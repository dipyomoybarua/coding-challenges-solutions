"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "[{()}{()()}]"
Output: true
"""

from enum import Enum

class Bracket(Enum):
    OPEN_PARENTHESIS = '('
    OPEN_SQUARE_BRACKET = '['
    OPEN_CURLY_BRACKET = '{'
    CLOSE_PARENTHESIS = ')'
    CLOSE_SQUARE_BRACKET = ']'
    CLOSE_CURLY_BRACKET = '}'

def is_valid(s: str) -> bool:
    # Mapping of closing to opening brackets using Enum
    bracket_map = {
        Bracket.CLOSE_PARENTHESIS: Bracket.OPEN_PARENTHESIS,
        Bracket.CLOSE_SQUARE_BRACKET: Bracket.OPEN_SQUARE_BRACKET,
        Bracket.CLOSE_CURLY_BRACKET: Bracket.OPEN_CURLY_BRACKET
    }
    
    # Convert the input string to a list of Enum values for easier comparison
    s_enum_values = [Bracket(value) for value in s]
    
    # Stack to track unmatched opening brackets, now holding Enum values
    stack = []
    
    for char in s_enum_values:
        if char in bracket_map.values():
            # If it's an opening bracket, push to the stack
            stack.append(char)
        elif char in bracket_map:
            # If it's a closing bracket
            if stack and stack[-1] == bracket_map[char]:
                # If it matches the top of the stack, pop it
                stack.pop()
    
    # Return True if the stack is empty (all brackets matched), False otherwise
    return not stack

# Test cases
print(is_valid("()")) 
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("[{()}{()()}]"))
