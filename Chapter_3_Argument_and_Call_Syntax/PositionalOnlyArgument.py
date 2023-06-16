def number_length(x, /):
    return len(str(x))

# should work
print(number_length(1222))

# shoud fail
print(number_length())