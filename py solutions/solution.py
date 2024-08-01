"""
Write a function solution that, given a string S of length N, returns any palindrome
which can be obtained by replacing all of the question marks in S by lowercase letters
(^ prime a' -^ prime z^ prime ) If no palindrome can be obtained, 
the function should return the string "NO".

A palindrome is a string that reads the same both forwards and backwards. 
Some examples of palindromes are: "kayak", "radar", "mom".

Examples:

1. Given S=^ prime prime ? ab ??a^ prime prime the function should return "aabbaa"

2. Given S=^ bab ??a^ prime prime . the function should return "NO".

3. Given S =^ prime prime ?a?^ prime prime . the function may return "aaa". 
It may also return "zaz", among other possible answers. 
The function is supposed to return only one of the possible answers.

Assume that:
• N is an integer within the range [1..1,000];

• string S consists only of lowercases letters ( a' -^ prime z^ prime ) or 7.

"""

def solution(S):
    N = len(S)
    S = list(S)  # Convert string to list to modify characters
    
    # Traverse from both ends towards the center
    for i in range(N // 2):
        left_char = S[i]
        right_char = S[N - 1 - i]  # Corrected index for right character
        
        if left_char == '?' and right_char == '?':
            S[i] = 'a'
            S[N - 1 - i] = 'a'
        elif left_char == '?':
            S[i] = right_char
        elif right_char == '?':
            S[N - 1 - i] = left_char
        else:
            if left_char != right_char:
                return "NO"
    
    # Check for odd-length strings
    if N % 2 != 0 and S[N // 2] == '?':
        S[N // 2] = 'a'
    
    return ''.join(S)

# Usage:
print(solution("??ab??a")) 
print(solution("bab??a"))  
print(solution("?a?"))  

