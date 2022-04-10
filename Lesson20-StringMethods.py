import pyperclip

string = 'String MEthods'
print(string)
print(string.upper())
print(string.lower())
print(string.title())
print(string.capitalize())

print(string.upper().isupper())
print(string.upper().islower())
print(string.isdecimal())
print(string[6].isspace())

pyperclip.copy('Hello')
print('Check if you can paste \'Hello\'')

print(','.join(['cats', 'rats', 'bats']))
print(' '.join(['cats', 'rats', 'bats']))

print('His name is Hank.'.split())
print('His name is Hank.'.split('H'))