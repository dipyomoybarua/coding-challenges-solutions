def find_largest_three(nums):
    # Initialize variables to store the three largest numbers
    largest = float('-inf')
    second_largest = float('-inf')
    third_largest = float('-inf')
    
    # Iterate through the list and update the largest numbers
    for num in nums:
        if num > largest:
            third_largest = second_largest
            second_largest = largest
            largest = num
        elif num > second_largest:
            third_largest = second_largest
            second_largest = num
        elif num > third_largest:
            third_largest = num
    
    # Return the largest three numbers
    return [largest, second_largest, third_largest]

# usage:
nums = [10, 5, 20, 15, 30]
result = find_largest_three(nums)
print("Largest three numbers:", result)
