"""Question: Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given number.

Here:-
1. Number sorted in assending order.
2.  We are looking for both asending & desending order
"""

def  binary_search(condition, low, high):
    while  low <= high:
        middle = (low + high) //2
        result = condition(middle)
        if   result == 'found':
            return middle
        elif result =='left':
            high = middle - 1
        else : 
            low = middle + 1
            return -1
        
def first_possition(nums, target):
    def condition(mid):
        if nums[mid]==target:
            if  mid >0 and nums[mid-1] == target:
                return 'left'
            return  'found'
        elif nums[mid] < target:
            return  'right'
        else:
            return 'left'
    return binary_search(0, len-1, condition)
    
def last_possition(nums,target):
    def condition(mid):
        if  nums[mid]==target:
            if mid < len(nums)-1 and nums[mid+1] == target :
                return "right"
            return "found"
        elif nums[mid] <= target:
            return "right"
        else:
            return "left"
    return binary_search(0,len(nums)-1,condition)
    
def first_and_last_possition(nums,target):
    return first_possition(nums,target), last_possition(nums,target)
        
