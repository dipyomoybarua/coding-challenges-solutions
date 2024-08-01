# List of contents
contents = [1, 2, 1, 1, 2, 3, 4]

# Initialize an empty dictionary to store counts
result_map = {}

# Iterate over the list and count occurrences of each element
for item in contents:
    if item in result_map:
        result_map[item] += 1
    else:
        result_map[item] = 1

print("M equal to:", result_map)
