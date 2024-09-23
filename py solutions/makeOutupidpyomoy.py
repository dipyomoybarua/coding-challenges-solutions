def transform_string(input_string):
    lower_case = input_string.lower()
    
    # Check if the string has at least three characters
    if len(lower_case) >= 3:
        # Extract the first two characters and the rest of the string
        first_two = lower_case[:2]
        rest_of_string = lower_case[2:]
        
        # Combine the second character (now first) with the first character, then add the rest of the string
        return first_two[::-1] + rest_of_string
    else:
        # If the string has less than three characters, return it as-is
        return lower_case

# Example usage
input_string = "Dipyomoy"
output = transform_string(input_string)
print(f"Input: {input_string}")
print(f"Output: {output}")
