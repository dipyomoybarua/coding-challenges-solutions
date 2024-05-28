fruits = {'apple': 2, 'banana': 3, 'orange': 1}
card = {'egg': 1, 'watermelon': 2, 'coconut': 1}
combined = card.copy()
for key, value in fruits.items():
    if key not in combined:
        combined[key] = value
    else:
        combined[key] += value
print(combined)
