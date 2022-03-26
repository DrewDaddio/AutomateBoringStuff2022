def example():
    print(range(0, 4))
    print(range(4))
    print([0, 1, 2, 3])
    print(list(range(4)))

    for i in range(4):
        print(i)

    supplies = ['pens', 'staplers', 'rabbits', 'trash can']
    for i in range(len(supplies)):
        print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


print(example())

#multiple assignment
Hank = ['white and brown', 'brave', 'male']
color, attitude, sex = Hank
print(Hank)
print(color)

color, attitude, sex = 'White and Brown', 'Brave', 'Male'
print(color)

a = 'AAA'
b = 'BBB'

print(a)
print(b)
a, b = b, a

print(a)
print(b)