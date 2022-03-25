name = ''
while name != 'Drew':
    print('Please type your name, Drew.')
    name = input()
print('Thank you ' + name + '!')

age = ''
while True:
    print('Please type your age of 36 yo: ')
    age = input()
    if age == '36':
        break
print('thanks for typing the age of ' + age)

spam = 0
while spam < 5:
    spam = spam +1
    if spam == 3:
        continue
    print('spam is ' + str(spam))