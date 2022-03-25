spam = 42 #global variable

def eggs():
    spam = 42 #local variable
    print(spam)

print(spam)
eggs()


bread = 30

def ham():
    print(bread)

def bacon():
    bread = 'Bacon'
    print(bread)

ham()
bacon()

def turkey():
    global bread
    bread = 'Turkey'
    print(bread)

turkey()
print(bread)