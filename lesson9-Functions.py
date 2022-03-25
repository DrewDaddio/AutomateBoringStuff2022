def hello():
    print('Hi')
    print('Hey')
    print('Hello')
    print('The above is function hello()')

def hello2(name):
    print('Hello ' + name)

hello()

hello2('Hank')
hello2('Dorothy')

print('The above 2 lines are function hello2()')

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

#inputNumber = plusOne(input('input a number: '))
#print(str(inputNumber))

#Print
print('Hello')
print('World')
print('Hello', end=' ')
print('World')
print('Hello', 'World')
print('Hello', 'World', sep='ABC')