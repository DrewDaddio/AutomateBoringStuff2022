import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

ExampleList = 'here is a list of phone numbers' \
              '111-222-3333' \
              '333-222-1111' \
              '333-222-1112' \
              '333-222-1113' \
            '555 323-2938' \
            '555 323-2939'

print(phoneRegex.findall(ExampleList))

phoneRegex2 = re.compile(r'(\d\d\d) (\d\d\d-\d\d\d\d)')
print(phoneRegex2.findall(ExampleList))

lyrics12Days = ''''On the first day of Christmas, my true love gave to me 1 partridge in a pear tree.
On the second day of Christmas my true love gave to me 2 turtle doves
and 1 partridge in a pear tree.
On the third day of Christmas my true love gave to me 3 French hens,
2 turtle doves, and 1 partridge in a pear tree.
On the 4th day of Christmas my true love gave to me
4 calling birds, 3 French hens, 2 turtle doves and 1 partridge in a pear tree.
On the fifth day of Christmas my true love gave to me 5 golden rings,
4 calling birds, 3 French hens, 2 turtle doves and 1 partridge in a pear tree.
On the 6th day of Christmas my true love gave to me 6 geese a laying,
5 golden rings, 4 calling birds, 3 French hens, 2 turtle doves
and 1 partridge in a pear tree.
On the 7th day of Christmas my true love gave to me 7 swans a swimming,
6 geese a laying, 5 golden rings, 4 calling birds, 3 French hens,
2 turtle doves and 1 partridge in a pear tree.
On the 8h day of Christmas my true love gave to me 8 maids a milking,
7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds,
3 French hens, 2 turtle doves and 1 partridge in a pear tree.
On the ninth day of Christmas my true love gave to me 9 ladies dancing,
8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings,
4 calling birds, 3 French hens, 2 turtle doves and 1 partridge in a pear tree.
On the 10th day of Christmas my true love gave to me 10 lords a leaping,
9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying,
5 golden rings, 4 calling birds, 3 French hens, 2 turtle doves
and 1 partridge in a pear tree.
On the 11th day of Christmas my true love gave to me 11 pipers piping,
10 lords a leaping 9 ladies dancing, 8 maids a milking, 7 swans a swimming,
6 geese a laying, 5 golden rings, 4 calling birds, 3 French hens,
2 turtle doves and 1 partridge in a pear tree.
On the 12 day of Christmas my true love gave to me 12 drummers drumming,
11 pipers piping, 10 lords a leaping 9 ladies dancing, 8 maids a milking,
7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds,
3 French hens, 2 turtle doves and 1 partridge in a pear tree.
'''

lyricsRegex = re.compile(r'\d+\s\w+')
print(lyricsRegex.findall(lyrics12Days))

uniqueRegex = re.compile(r'[x-zA-F]')
print(uniqueRegex.findall(lyrics12Days))