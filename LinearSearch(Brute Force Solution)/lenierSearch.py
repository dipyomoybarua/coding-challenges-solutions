"""To find the card in decreasing order & since the card is in face down possition in a table ,
we need to pic the card in less turn possition"""

"""Approach to solve the problem:-
1. Create a variable possition with initialize value as 0
2. Check whether we've reached the end of the array before trying to access an element.
3. If it is equal then possition from the function can be returned from the function
4. If it is not equal then incriment the possition by 1 & then repeat the step 2 to n until we get the result.
5. If the element is nit yet found then return -1 """

def find_card(cards, query):
    # Initialize position of card and query
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    if  position >= len(cards):
        return -1

# Test cases
cards = [10, 8, 6, 4, 2]
query = 6
print("Test 1:", find_card(cards, query))

cards = [19, 16, 14, 9, 6, 4, 1]
query = 9
print("Test 2:", find_card(cards, query))

cards = [19, 16, 14, 11, 6, 4, 1]
query = 1
print("Test 3:", find_card(cards, query))

cards = [7]
query = 7
print("Test 4:", find_card(cards, query))

cards = [19, 16, 14, 11, 6, 4, 1]
query = 9
print("Test 5:", find_card(cards, query))

cards = []
query = 5
print("Test 6:", find_card(cards, query))

cards = [7, 7, 5, 3, 3, 1, 1]
query = 3
print("Test 7:", find_card(cards, query))

cards = [7, 5, 3, 3, 1]
query = 3
print("Test 8:", find_card(cards, query))

cards = [10, 8, 6, 4, 2]
query = 12
print("Test 9:", find_card(cards, query))

cards = [10, 8, 6, 4, 2]
query = 1
print("Test 10:", find_card(cards, query))

cards = list(range(1000000, 0, -1))
query = 987654
print("Test 11:", find_card(cards, query))
