def find_two_sum(nums, target):
    num_set = set()
    for num in nums:
        complement = target - num
        if complement in num_set:
            return [nums.index(complement), nums.index(num)]
        num_set.add(num)
    return "No 2 sum digit found"

# usage:
nums = [10, 5, 3, 4, 7]
target = 10
output = find_two_sum(nums, target)
print(output)
