"""Define an diamond shape """

def generate_alphabet_diamond(n):
    if n <= 0:
        return "Invalid Input"
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    diamond = []

    for i in range(n):
        leading_spaces = " " * (n - i - 1)
        alphabets = " ".join(alphabet[j] for j in range(i + 1))
        row = leading_spaces + alphabets
        diamond.append(row)

    for i in range(n - 2, -1, -1):
        leading_spaces = " " * (n - i - 1)
        alphabets = " ".join(alphabet[j] for j in range(i + 1))
        row = leading_spaces + alphabets
        diamond.append(row)

    return "\n".join(diamond)

print(generate_alphabet_diamond(5))
