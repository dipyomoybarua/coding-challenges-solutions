"""Binary search:
How we should find the solution:-
1. Find the middle element.
2. If it matches the query number then return the middle position as the answer.
3. If the number is less than the query number then search the 1st half of the list.
4. If the number is more then the queried number then search the 2nd half of the list.
5. If no element is to be reurned then return -1 """

def test_location(card,query,mid):
    mid_number = card[mid]
    if mid_number == query :
        if mid -1  >=0 and card[mid-1] == query:    
            return 'left'
        else:
            return 'found'
    elif mid_number < query :
        return 'left'
    else:
        return 'right'
    
def locate_card(card,query):
    low = 0
    high = len(card)-1
    while low<=high:
        mid = (low+high)//2
        side=test_location(card,query,mid)
        
        if side == 'found':
                return mid
        elif side=='left':
            high = mid-1
        elif side =='right':
            low = mid+1
            
            return -1

# Test cases
cards = [10, 8, 6, 4, 2]
query = 6
print("Test 1:", locate_card(cards, query))

cards = [19, 16, 14, 9, 6, 4, 1]
query = 9
print("Test 2:", locate_card(cards, query))

cards = [19, 16, 14, 11, 6, 4, 1]
query = 1
print("Test 3:", locate_card(cards, query))

cards = [7]
query = 7
print("Test 4:", locate_card(cards, query))

cards = [19, 16, 14, 11, 6, 4, 1]
query = 9
print("Test 5:", locate_card(cards, query))

cards = []
query = 5
print("Test 6:", locate_card(cards, query))

cards = [7, 7, 5, 3, 3, 1, 1]
query = 3
print("Test 7:", locate_card(cards, query))

cards = [7, 5, 3, 3, 1]
query = 3
print("Test 8:", locate_card(cards, query))

cards = [10, 8, 6, 4, 2]
query = 12
print("Test 9:", locate_card(cards, query))

cards = [10, 8, 6, 4, 2]
query = 1
print("Test 10:", locate_card(cards, query))

cards = list(range(1000000, 0, -1))
query = 987654
print("Test 11:", locate_card(cards, query))

