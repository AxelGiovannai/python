test=[1,1,1,0,0,0,0,2,2,2,2]        #swap en python


def initboard(n,p):
    board = [0] * n
    if p>=(n/2):
        p = int((n/2) - 1)
    for i in range(0,p):
        board[i] = 1
    for i in range(n-1,((n-1)-p),-1):
        board[i] = 2
    return board
    
def display(board, n):

    lengths = [len(str(i)) for i in range(1,n+1)]

    for i in range(n):
        symbol = ""
        if board[i] == 0:
            symbol = '.'
        elif board[i] == 1:
            symbol = 'o'
        elif board[i] == 2:
            symbol = 'x'
        print(' ' * (lengths[i] - 1) + symbol, ' ', end=' ')
    print()

    for i in range(1,n+1):
        print(i, ' ', end=' ')
    print()

def possible(board,n,i,player):
    
