athletes = ['Michael Jordan', 'Scottie Pippen', 'Horace Grant', 'BJ Simpson', 'Larry Bird', 'John Stockton']

print(sorted(athletes, key=lambda name: name.split()[-1]))

last_name = lambda name: name.split()[-1]
print(last_name('Ray Maldonado'))

print('That is the same as doing it with a definition: ')


def last_Name(name):
    return name.split()[0]


print(last_Name('Ray Maldonado'))

print(callable(last_Name))
print(callable(athletes))
