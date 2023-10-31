test = [0 , 1 , 0 , 0 , -1 , 0 , 1 , 0 , -1 , 0 , 1 , 1 , 0 , -1, -1]   #15
testp = [1 , 1 , 1 , 1]
test2 = [0 , 0 , 0 , 0 , 0]

def newboard(n):
    board = [0] * n
    return board

 
def display(board, n):

    lengths = [len(str(i)) for i in range(1,n+1)]

    for i in range(n):
        symbol = ""
        if board[i] == 0:
            symbol = '.'
        elif board[i] == -1:
            symbol = 'o'
        elif board[i] == 1:
            symbol = 'x'
        print(' ' * (lengths[i] - 1) + symbol, ' ', end=' ')
    print()

    for i in range(1,n+1):
        print(i, ' ', end=' ')
    print()


def possible(board,n,i):
    if board[i-1] == 0:
        return True 


def select(board,n):
    i= eval(input("Choose a licit number of square : "))
    if 0<i<(len(board)+1):
        return i
    else:
        select(board,n)


def put(board,n,i):
    board[i-1] = 1
    if i != 1:
        board[i-2] = -1
    if i != n:
        board[i] = -1


def again(board,n):
    for i in range(n):
        if board[i] == 0:
            return True
    return False


def Dawson(n):

    player = 0
    board = newboard(n)
    display(board,n)

    while again(board,n) == True:
        if player%2 ==0:
            print("Player 1 ")
            print()
        else:
            print("player 2")
            print()

        player += 1    
        i = select(board,n)

        if possible(board,n,i) == True:
            put(board,n,i)
            display(board,n)
    if player%2 == 0:
        print("player 2 win")
    else:
        print("player 1 win") 
    

