
import re, pyperclip

#Create a regex for phone numbers
phoneRegex = re.compile(r'''
#Examples to find: 415-555-0000, (415) 555-0000, 555-000 ext 123, ext. 13432, x 13143
(((\d\d\d)|(\(\d\d\d\)))?            # Area code (optional)
(\s|-)            # First separator
\d\d\d           # First 3 digits
-            # Separator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s)|x)            # Extension word part (Optional)
    (\d{2,5}))?)            # Extension number part (Optional)
''', re.VERBOSE)

#Create a regex for email addresses
emailRegex = re.compile(r'''
#example: Drew.daddio@github.com
[a-zA-Z0-9_.+]+ # name part
@ # @symbol
[a-zA-Z0-9_.+]+ #domain Name
''', re.VERBOSE)

#Get the text off the clipboard
text = pyperclip.paste()
text = '''
Jessie Mckay jmckay67@aol.com 479-205-4874
Tom Jordan tjordan@msn.com 678-560-3485
Clayton Cross ccross20@gmail.com 724-900-2986
Rayford Sutton rayfords66@hotmail.com 242-391-3183
Jerome Gentry jgentry@me.com 604-720-6426
Weldon Camacho wcamacho57@icloud.com 651-807-8065
'''
#Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail)

allPhoneNumbers = []
for i in extractedPhone:
    allPhoneNumbers.append(i[0])

#Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
print(results)