import re

beginWithHelloRegex = re.compile(r'^Hello')
print(beginWithHelloRegex.search('Hello world!'))

endWithWorldRegex = re.compile(r'world!$')

print(endWithWorldRegex.search('Hello world!'))

allDigitsRegex = re.compile(r'^\d+$')
allDigits = '243423424322'
notAllDigits = '243423x424322'
print(allDigitsRegex.search(allDigits))
print(allDigitsRegex.search(notAllDigits))

atRegex = re.compile(r'.at')
at = 'The cat in the hat ate at the mat'
print(atRegex.findall(at))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameExample = 'First Name: Drew Last Name: Daddio'
print(nameRegex.findall(nameExample))

serve = '<To serve humans> for dinner.>'
firstRegex = re.compile(r'<(.*?)>')
secondRegex = re.compile(r'<(.*)>')

print(firstRegex.findall(serve))
print(secondRegex.findall(serve))