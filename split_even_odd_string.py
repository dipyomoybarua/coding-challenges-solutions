str = "asdfghjkldgvhgdvchgvd"

def split_odd_even(input_string):
    odd_char = input_string[::2]
    even_char = input_string[1::2]
    return odd_char,even_char

input_string= "asdfghjkl"
odd_char,even_char = split_odd_even(input_string)
print("odd char are:- ",odd_char)
print("the even  char are:-",even_char)
