def hypervolume(*args):
    print(args)
    print(type(args))

def hypervolume_improved(lenghth, *lenghts):
   v = lenghth
   for item in lenghts:
        v *= item
        return v


hypervolume(3,4)

print(hypervolume_improved(3,5,5,1))