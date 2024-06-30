def fill_none_values(arr):
    filled_arr = []
    prev_value = None
    
    for item in arr:
        if item is not None:
            prev_value = item
        filled_arr.append(prev_value)
    
    return filled_arr

# Usage
array1 = [1, None, 2, 3, None, None, 5, None]
output = fill_none_values(array1)
print(output) 
