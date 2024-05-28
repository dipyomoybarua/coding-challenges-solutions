"""Here is the problem statement to impliment the generic binary search
 so that it can be used in many problem 
  Approach:- 
   1. Come u with a solution function to determine the possition of the point whether
    it is at the before or after at a given point
   2. Retrive the mid point & the element in the list.
   3. If the answer returns the mid possition.
   4. If the answer lies in the left/before possition then repeat the search in the first half of the list.
   5. If the answer lies in the right/ater possition then repeat the search in the second half of the list. 
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

def locate_card(cards, query):
    
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    
    return binary_search(0, len(cards) - 1, condition)