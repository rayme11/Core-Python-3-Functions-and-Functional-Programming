def print_args(arg1, arg2, arg3, *args):
    print(arg1)
    print(arg2)
    print(arg3)
    print(args)

t = (12, 13, 14, 15,16)
print(print_args(*t))