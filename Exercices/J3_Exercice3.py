magiqueV = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]  #total: 45    L1:15
magiqueF = [[4, 9, 8], [9, 5, 1], [2, 7, 6]]

def sumTotal(square,n):
    Somme = 0
    for i in range(n):
        for j in range(n):
            Somme += square[i][j]
    return Somme

def checkRow(square,n,j,x):
    Somme = 0
    for i in range(n):
        Somme += square[i][j]
    if Somme == x:     #return (somme == x)
        return True
    else:
        return False 
    
def checkColumn(square,n,i,x):
    Somme = 0
    for j in range(n):
        Somme += square[i][j]
    if Somme == x:
        return True
    else:
        return False
    
def checkdiagonal(square,n,d,x):
    reverseI = n - 1
    Somme = 0
    if d%2 == 0:
        for i in range(n):
            Somme += square[i][i]
    else:
        for j in range(n):
            Somme += square[reverseI][j]
            reverseI += -1
    if Somme == x:
        return True
    else:
        return False


def magic(square):
    n = len(square)
    x = sumTotal(square,n)/n
    if checkdiagonal(square,n,1,x) == False or checkdiagonal(square,n,2,x) == False:
        return False
    else:
        for i in range(n):
            if checkRow(square,n,i,x) == False or checkColumn(square,n,i,x) == False:
                return False
            else:
                return True
        
            
def magicNormal(square):
    stop_boucle_interne = False
    n = len(square)
    m = [False] * ((n * n)+1)
    if magic(square) == False:
        return False
    else:
        for i in range(n):
            for j in range(n):
                if m[square[i][j]] == False:
                    m[square[i][j]] = True
                else:
                    stop_boucle_interne = True
        if stop_boucle_interne:
            return False
        else:
            return True
        
