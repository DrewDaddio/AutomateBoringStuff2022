print(list('Hank'))

name = 'Hank'
print(name)
print(name[0])
print(name[1:3])
print(name[-1])
print('H' in name)

#splice
declare = 'Dorothy is a rabbit'
print(declare)
newDeclare = declare[0:7] + ' the ' + declare[-6:-1] + 't'
print(newDeclare)

spam = [0, 1, 2, 3, 4, 5]
print(spam)
cheese = spam
print(cheese)
cheese[1] = 'Hello'
print(cheese)
print(spam)

def breakfast(someParameter):
    someParameter.append('Hello')

breakfast(spam)
print(spam)

import copy
exampleCopy = ['a', 'b', 'c', 'd']
print(exampleCopy)

support = copy.deepcopy(exampleCopy)
print(support)

support[1] = 10000
print(exampleCopy)
print(support)