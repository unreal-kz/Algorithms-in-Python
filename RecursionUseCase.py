# Find the length of the string

sample = "Hello"

def find_len_recursively(my_string):

    if my_string == "":
        return 0
    return 1 + find_len_recursively(my_string[1:])

# print (find_len_recursively(sample))


# Reverse the string

def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0]

# print(sample[0:])
# print(reverse(sample))