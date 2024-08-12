"""Customer support for an e-commerce business uses a computerized algorithm 
for evaluating if support tickets are still open.

Open and closed tickets are represented by different open and closed braces respectively.
For example, each of the braces Y // represent an open ticket and need matching braces') 
//' in that order to close them.

The braces in a string are balanced if the following conditions are met:

• All open braces must be closed

• Each closed brace must have a matching open brace

Any set of nested braces must be closed before its surrounding braces

Given a 2-dimensional array of strings comprised of braces, 
verify that the braces in each string are balanced. 
Return 'YES' if the braces are balanced and 'NO' otherwise.

Example

braces=()[]{}

• The braces in the first string '10)' are balanced,
because all braces are closed and all nested braces are closed in order.

• The braces in the second string '([])' are not balanced,
because the nested brace' was not closed before its surrounding '[]', 
so the order was not respected.

• The result is ['YES', 'NO']

Function Description Complete the function matching Braces in the editor below.

matchingBraces has the following parameter(s):

string braces[n]: an array of strings to analyze

Returns:

string(): an array of strings, eaither 'YES'or 'NO', 
where the string at each index /denotes whether the braces are balanced in bracesfit

"""

MATCHING_BRACKET = {')': '(', ']': '[', '}': '{'}

def is_balanced(braces_string):
    stack = []
    for char in braces_string:
        if char in MATCHING_BRACKET.values():
            stack.append(char)
        elif char in MATCHING_BRACKET:
            if stack and stack[-1] == MATCHING_BRACKET[char]:
                stack.pop()
            else:
                return 'NO'
    return 'YES' if not stack else 'NO'

def matchingBraces(braces_list): 
    # Process a list of brace strings and return a list of balance results
    results = []
    for brace_string in braces_list:  
        results.append(is_balanced(brace_string))  
    return results

#usage
braces = ["()[]{}", "([{}])", "(]", "{[()]}", "([)]"]
print(matchingBraces(braces))  