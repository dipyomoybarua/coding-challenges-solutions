def is_palindrom(num):
    if num <0:
        return False # Handle negative numbers 
        
    orginal_num = num
    reverse_num = 0
        
    while num > 0:

        last_digit = num % 10 # Extract the last digit
        
        reverse_num = reverse_num * 10 + last_digit # Build the reversed number
        num = num // 10  # Remove the last digit from the original number
    return orginal_num == reverse_num # Compare original and reversed numbers
print(is_palindrom(545))