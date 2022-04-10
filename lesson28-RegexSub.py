import re

namesRegex = re.compile(r'Agent \w+')
names = 'Agent Drew and Agent Hank'
print(namesRegex.sub('Redacted', names))

namesRegex2 = namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex2.findall(names))

print(namesRegex2.sub(r'Agent \1***', names))