def find_min_in_rotating_array(nums):
    start,end = 0, len(nums) -1
    while start < end:
        mid = (start+end)//2
        
        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid
            
    return nums[start]
    
rotating_array = [4, 5, 6, 7, 8, 9, 13, 1]
print(find_min_in_rotating_array(rotating_array))
 