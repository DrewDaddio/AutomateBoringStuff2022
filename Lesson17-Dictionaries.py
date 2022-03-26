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