# Local function will create a new instance
# each time last_letter is called with new string

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]

    print(last_letter)
    return sorted(strings, key=last_letter)


print(sort_by_last_letter(['ray', 'hello', 'world', 'a', 'b', 'c']))
print(sort_by_last_letter(['ray', 'hello', 'world', 'a', 'b', 'c']))

# e..g output:
#
# <function sort_by_last_letter.<locals>.last_letter at 0x1027abb80>
# ['a', 'b', 'c', 'world', 'hello', 'ray']
# <function sort_by_last_letter.<locals>.last_letter at 0x1027abb80>
# ['a', 'b', 'c', 'world', 'hello', 'ray']
