family = ['Drew', 'Erin', 'Hank', 'Dorothy']

print(family)
print(family[0])
print(family[1])
print(family[2])
print(family[3])
print(family[-1])

rabbits = ['Frodo', 'Marble', ['Dancer', 'Prancer'], ['Blossom', 'Ducati'], 'Pancake', 'Hank', 'Dorothy']

print(rabbits)
print(rabbits[2])
print(rabbits[2][0])

rabbits[2][1] = 'Hank'
print(rabbits)

group = family + rabbits
print(group)

print('Hank' in rabbits)