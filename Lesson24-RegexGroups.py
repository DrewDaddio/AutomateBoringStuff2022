import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

message = 'my phone numbers are 201-247-2983 or 201-317-5843'

mo = phoneNumRegex.search(message)

print(mo.group())

groupRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = groupRegex.search(message)

print(mo2.group())
print(mo2.group(1))
print(mo2.group(2))

groupRegex2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
message2 = 'my phone number is (201) 237-2983'
mo3 = groupRegex2.search(message2)
print(mo3.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
bat = batRegex.findall('the Batmobile lost a wheel so Batman rode the Batcopter')
print(bat)