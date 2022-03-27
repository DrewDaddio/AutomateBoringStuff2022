import pprint

Hank = {'Color': 'white and brown', 'attitude': 'brave', 'Sex': 'male'}
print(Hank)

print('Hank has ' + Hank['Color'] + ' fur')

print(list(Hank.keys()))
print(list(Hank.values()))
print(list(Hank.items()))

def hankkeys():
    for k in Hank.keys():
        print(k)

def hankvalues():
    for v in Hank.values():
        print(v)

def hankitems1():
    for k, v in Hank.items():
        print(k, v)

def hankitems2():
    for i in Hank.items():
        print(i)

print(hankkeys())
print(hankvalues())
print(hankitems1())
print(hankitems2())

Hank.setdefault('Size', 'tiny')
print(hankitems2())

#message: count characters

def countMessage():
    message = 'It was a bright cold day in April, and the really large clocks were striking thirteen.'
    count = {}

    for character in message.upper():
        count.setdefault(character, 0)
        count[character] = count[character] + 1

    print(count)
    pprint.pprint(count)

countMessage()

