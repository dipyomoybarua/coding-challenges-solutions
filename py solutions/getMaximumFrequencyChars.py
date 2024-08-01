"""Write a Python function that gets a string value as input, and return a string that 
contains all chars with maximum appearances (char should be printed once).
s1 = "gcccggd" -> res_s = "gc"                          
s2 = "gcccggdg" -> res_s = "g"
s3 = "HelloOo World" -> res_s = "lo"
"""

def get_maximum_frequency_chars(s):
    # initialize an empty dictto store chars freq.
    frequency = {}
    # iterate through each char in the input string
    for char in s:
# Update the frequency count for charecter
        frequency[char] = frequency.get(char,0) + 1
        max_frequency = max(frequency.values(),default=0)
    max_freq_chars = [char for char , freq in frequency.items() if freq == max_frequency]
    return ''.join(max_freq_chars)

s1 = "gcccggd"
s2 = "gcccggdg"
s3 = "HelloOo World"

print(get_maximum_frequency_chars(s1))
print(get_maximum_frequency_chars(s2))
print(get_maximum_frequency_chars(s3))