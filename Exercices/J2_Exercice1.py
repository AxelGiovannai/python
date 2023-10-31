#Exercice 2

def Pyramide_etoile_1():
    h = eval(input("hauteur de la pyramide : "))
    for i in range(h,0,-1):
        print(i*'*')

#Exercice 3

def Pyramide_etoile_2():
    h = eval(input("hauteur de la pyramide : "))
    for i in range(h):
        print((h-i-1)*' '+i*'*')
    
def pyramide():
    rows = eval(input('Nombre de ligne : '))
    offset = rows - 1
    currentRow = 1
    while (offset >= 0):
        print(' '*offset, '*'*(currentRow * 2 - 1), sep='',end='7')
        offset -= 1
        currentRow += 1

#Exercice 4.1

def Table_Exotique_1():
    h = eval(input("hauteur de la pyramide : "))
    for i in range(1,h+1):
        print(i*'1',' * ',i*'1',' = ',end=' ')
        for j in range(1,i):
            print(j,end=' ')
        for j in range(i,0,-1):
            print(j,end=' ')
        print()

#Exercice 4.2

def Table_Exotique_2():
    h = eval(input("hauteur de la pyramide : "))
    for i in range(1,h):
        print("9 * ",end=' ')
        for j in range(1,i):
            print(j,end=' ')
        print(" + ",i+1,end=' ')
        for j in range(1,i):
            print((j+1)*'1',end=' ')
        print()


