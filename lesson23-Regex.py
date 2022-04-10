import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

def isPhoneNumber(text):
    if len(text) !=12:
        return False # not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3] != '-':
        return False #missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False #no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False #missing last 4 digits
    return True


print(isPhoneNumber('hello'))
print(isPhoneNumber('201-247-2983'))

message = 'my phone numbers are 201-247-2983 or 201-317-5843'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('phone number: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('could not find any phone numbers')

print(message)

mo = phoneNumRegex.search(message)
print(mo.group())

moAll = phoneNumRegex.findall(message)
print(moAll)