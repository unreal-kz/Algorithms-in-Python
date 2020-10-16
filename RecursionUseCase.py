# Find the length of the string

sample = "Hello, world!!!"

def find_len_recursively(my_string):

    if my_string == "":
        return 0
    return 1 + find_len_recursively(my_string[1:])

print (find_len_recursively(sample))
