athletes = ['Michael Jordan', 'Scottie Pippen', 'Horace Grant', 'BJ Simpson', 'Larry Bird', 'John Stockton']

print(sorted(athletes, key=lambda name: name.split()[-1]))

last_name = lambda  name: name.split()[-1]
print(last_name('Ray Maldonado'))