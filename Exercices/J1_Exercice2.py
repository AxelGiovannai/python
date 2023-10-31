#import
import random

#Exercice 1 

def MaxMin():
    a = eval(input("Premier nombre :"))
    b = eval(input("Second nombre :"))
    if a > b:
        print("Maximum : "+  str(a))
        print("Minimum : "+ str(b))
    elif a <b:
        print("Maximum : "+str(b))
        print("Minimum : "+str(a))
    else:
        print(str(a)+" est egal a "+str(b))

#Exercice 2

def Remise():
    Prix = eval(input("Prix de l'article : "))
    if Prix < 0:
        print("Erreur")
    elif (Prix >= 100 and Prix <= 500):
        Prix = Prix * (1-(5/100))
        print("Votre prix est de : "+ str(Prix))
    elif Prix > 500:
        Prix = Prix * (1-(8/100))
        print("Votre prix est de : "+ str(Prix))
    else:
        print("Votre prix est de : "+ str(Prix))

#Exercice 3

def Tries():
    a = eval(input("Numbre 1 : "))
    b = eval(input("Numbre 2 : "))
    c = eval(input("Numbre 3 : "))
    if (a<b<c):
        return True
    else:
        return False

#Exercice 4

def Tri():
    a = eval(input("Numbre 1 : "))
    b = eval(input("Numbre 2 : "))
    c = eval(input("Numbre 3 : "))
    while not (a<b<c): 
        if a>b:
            a,b=b,a
        if b>c:
            b,c=c,b
    return print("Les nombres dans l'ordre croissant sont : "+str(a)+" , "+str(b)+" , "+str(c))

# Exercice 4 - Tri de 3 nombres

a = eval(input('Entrez le nombre A : '))
b = eval(input('Entrez le nombre B : '))
c = eval(input('Entrez le nombre C : '))
if a > c:

  a,c = c,a
if a > b:

  a,b = b,a
if b > c:

  b,c = c,b
print(a, b, c)
            

#Exercice 5

def Signe_produit():
    a = eval(input("Numbre 1 : "))
    b = eval(input("Numbre 2 : "))
    if (a>=0 and b>=0) or (a<=0 and b<=0) :
        print("Positif")
    else:
        print("Negatif")

    
#Exercice 6

def n_premiers_entiers():
    a = eval(input("Nombre : "))
    total = 0
    for  i in range(a):
        total += i 
    return total

#Exercice 7

def Somme_terminant_zero():
    somme = 0
    while True:
        nombre = eval(input("Entrer un nombre :"))
        if nombre == 0:
            break
        somme += nombre
    print("la somme de nombre est : "+ str(somme))



#Exercie 8

def sum_entiers_pairs():
    a = eval(input("Nombre : "))
    total = 0
    for  i in range(1,a+1):
        if 0==i%2:
            total += i
        else:
            total += 0    
    return total

#Juste Prix

def juste_prix():
    random_price = random.randint(1,100)
    attempt = 7
    while attempt>0:
        test = eval(input("Prix suggerer : "))
        if test==random_price:
            return(print("Bravo !"))
        elif test>random_price:
           print("trop grand! il vous reste ",attempt -1,"tentative")
        elif test<random_price:
            print("trop petit! il vous reste ",attempt -1,"tentative")

            attempt-=1
            if attempt == 0:
                print("trop nul")            


def moyenne():
    total_number = eval(input("nombre de nombre que vous souhaitez rentrer : "))
    for i in range(1,total_number+1):
         nombre = eval(input("Entrer un nombre :"))
