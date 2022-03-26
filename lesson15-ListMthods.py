spam = ['Hi', 'hey', 'hello', 'hola', 'howdy']

print(spam.index('hey'))

animals = ['rabbit', 'dog', 'cat']
print(animals)

animals.append('bird')
print(animals)

animals.insert(1,'seal')
print(animals)

animals.append('seal')
animals.append('seal')
print(animals)
animals.remove('seal')
print(animals)

del animals[4]
print(animals)

numbers = [2, 5, 3.14, 1, -7]
print(numbers)
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)