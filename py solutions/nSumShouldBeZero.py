"""
Write a function

def solution(N)

that, given an integer N (1 <= N <= 100) returns an array containing 
N unique integers that sum up to 0. The function can return any such array.

For example, given N = 4 the function could return 
[1, 0, - 3, 2 ] or [- 2, 1, - 4, 5] The answer [1, - 1, 1, 3] 
would be incorrect (because value 1 occurs twice).
For N = 3 one of the possible answers is [- 1, 0, 1] 
but there are many more correct answers).
"""

def solution(N):
    result = []
    
    # Generate pairs for even N
    for i in range(1, N // 2 + 1):
        result.append(i)
        result.append(-i)
    
    # If N is odd, add 0 to the result
    if N % 2 != 0:
        result.append(0)
    
    return result

# Function Use
print(solution(1)) 
print(solution(2)) 
print(solution(3)) 
print(solution(4)) 
print(solution(5)) 
print(solution(100))
