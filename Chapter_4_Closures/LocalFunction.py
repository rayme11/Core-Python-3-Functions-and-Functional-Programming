def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    return sorted(strings, key=last_letter)

print(sort_by_last_letter(['ray', 'hello', 'world', 'a', 'b', 'c']))