def common_letters(str1, str2):
    # Convert strings to sets of characters to find common elements
    set1 = set(str1)
    set2 = set(str2)
    
    # Find intersection of the two sets to get common characters
    common = set1.intersection(set2)
    
    # Print common characters, each on a new line
    for char in common:
        print(char)

#usage:
string1 = "Hello"
string2 = "How are you"

print("Common letters:")
common_letters(string1, string2)
