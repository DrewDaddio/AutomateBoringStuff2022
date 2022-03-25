def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero', end=' ')


print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

def rabbits():
    print('How many rabbits do you have: ')
    numBuns = input()
    try:
        if int(numBuns) >= 3:
            print('That\'s a lot of bunnies')
        elif int(numBuns) < 0:
            print('You cannot have a negative amount of buns')
        else:
            print('You should get some more buns')
    except ValueError:
        print('You did not enter a number')


rabbits()