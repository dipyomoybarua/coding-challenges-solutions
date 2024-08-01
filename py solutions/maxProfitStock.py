"""
You are given the prices of a stock for the next 7 days. 
The goal is to determine the maximum profit you can achieve by buying and selling
the stock within these 7 days. 
"""

def max_profit(prices):
    if not prices:
        return 0  # Return 0 if the input list is empty
    
    min_price = float('inf')  # Initialize min_price to infinity
    max_profit = 0  # Initialize max_profit to 0
    
    for price in prices:
        if price < min_price:
            min_price = price  # Update min_price if current price is lower
        elif price - min_price > max_profit:
            max_profit = price - min_price  # Update max_profit if current profit is higher
            
    return max_profit

# prices for 7 days
prices = [100, 80, 150, 220, 300, 350, 80]

# Calculate the maximum profit
print(f"Maximum profit: {max_profit(prices)}")
