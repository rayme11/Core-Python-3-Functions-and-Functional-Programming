def enclosing():
    def local_func():
        print('local function')
    return local_func

lf = enclosing()
lf()