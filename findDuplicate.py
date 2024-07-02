def find_duplicate(arr):
    seen = set()
    duplicate = []
    for num in arr:
        if num in seen:
            duplicate.append(num)
        else:
            seen.add(num)
    return duplicate

# Find Duplicate
let_array = [1,2,3,1,2,9]
print(find_duplicate(let_array))
