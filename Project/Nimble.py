import random

test = [1, 6, 2, 8, 3, 2, 2]
n= 7

def newboard(n,p):
    board = [random.randint(0, p) for _ in range(n)]
    return board


def display(board,n):
    lengths = [len(str(i)) for i in range(1,n+1)]

    for i in range(n):
        if board[i]<9:
            print(' ',' ' * (lengths[i] - 1) + str(board[i]), ' ', end='|')
        else:
            print(' ',' ' * (lengths[i] - 1) + str(board[i]),'', end='|')
    print()

    for i in range(n):
        print('-' * ((lengths[i]+2)*2), end='')
    print()

    for i in range(1,n+1):
        print(' ',i, ' ', end='|')
    print()

