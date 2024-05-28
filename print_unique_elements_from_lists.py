L1 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 5, 6]

# Count occurrences of each element
number_count = {}
for element in L1:
    if element in number_count:
        number_count[element] += 1
    else:
        number_count[element] = 1

# Print unique elements and their counts before removal
print("Before removal:")
for element, count in number_count.items():
    print(f"{element} - Count: {count}")

# Create a new list with unique elements
unique_elements = list(number_count.keys())


print("\nAfter removal:")
print(unique_elements)
