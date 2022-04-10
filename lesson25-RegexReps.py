import re

batRegex = re.compile(r'Bat(wo)?man')

mo = batRegex.search('The adventures of Batman')
print(mo.group())

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

#mo7 = batRegex.search('The adventures of Batwowowowowoman')
#print(mo7.group())

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
moPN = phoneRegex.search('my phone number is 102-111-2232')
print(moPN.group())

phoneRegex2 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
moPN2 = phoneRegex2.search('my phone number is 111-2232')
moPN3 = phoneRegex.search('my phone number is 102-111-2232')
print(moPN2.group())
print(moPN3.group())

batRegex2 = re.compile(r'Bat(wo)*man')
mo4 = batRegex2.search('The adventures of Batman')
print(mo4.group())

mo5 = batRegex2.search('The adventures of Batwoman')
print(mo5.group())

mo6 = batRegex2.search('The adventures of Batwowowowowoman')
print(mo6.group())

batRegex3 = re.compile(r'Bat(wo)+man')
print(batRegex3.search('Batman'))
print(batRegex3.search('Batwoman'))
print(batRegex3.search('Batwowowoman'))

regex = re.compile(r'\+\*\?')
print(regex.search('I learned about +*? regex syntax'))

regex2 = re.compile(r'(\+\*\?)+')
print(regex2.search('I learned about +*?+*?+*?+*?+*?+*?+*? regex syntax'))

haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('He said HaHaHa'))