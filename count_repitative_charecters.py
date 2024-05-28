def count_repetitive_characters(input_string):
    # Create a dictionary to store character frequencies
    char_freq = {}

    # Count frequencies of each character in the string
    for char in input_string:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Filter characters with frequencies greater than 1 (repetitive characters)
    repetitive_chars = {char: freq for char, freq in char_freq.items() if freq > 1}

    return repetitive_chars


name = "My_name_is_Dipyomoy"
repetitive_chars = count_repetitive_characters(name)
print("Repetitive characters:", repetitive_chars)
