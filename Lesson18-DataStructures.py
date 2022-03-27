import pprint

Hank = {'Name': 'Hank', 'Color': 'white and brown', 'attitude': 'brave', 'Sex': 'male'}
Dorothy = {'Name': 'Dorothy', 'Color': 'Grey and Brown', 'attitude': 'skittish', 'Sex': 'female'}
print(Hank)
print(Dorothy)

Buns = []
print(Buns)
Buns.append({'Name': 'Hank', 'Color': 'white and brown', 'attitude': 'brave', 'Sex': 'male'})
print(Buns)
Buns.append({'Name': 'Dorothy', 'Color': 'Grey and Brown', 'attitude': 'skittish', 'Sex': 'female'})
print(Buns)

#Tic-Tac-Toe
theBoard = {
    'Top-L': 'X', 'Top-M': ' ', 'Top-R': ' ',
    'Mid-L': ' ', 'Mid-M': 'X', 'Mid-R': ' ',
    'Low-L': ' ', 'Low-M': ' ', 'Low-R': 'X'
}

pprint.pprint(theBoard)
def printBoard(board):
    print(board['Top-L'] + '|' + board['Top-M'] + '|' + board['Top-R'])
    print('-----')
    print(board['Mid-L'] + '|' + board['Mid-M'] + '|' + board['Mid-R'])
    print('-----')
    print(board['Low-L'] + '|' + board['Low-M'] + '|' + board['Low-R'])

printBoard(theBoard)