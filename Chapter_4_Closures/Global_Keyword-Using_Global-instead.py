message = 'global'

def enclosing():
    message = 'enclosing from enclosing def'

    def local():
        global message
        message = 'local change'

    print('enclosing message from enclosing def:', message)
    local()
    print('enclosing message from enclosing def:', message)

print('global message, from global:', message)
enclosing()
print('global message, after calling local global change:', message)