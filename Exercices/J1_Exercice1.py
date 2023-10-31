#Exercice 1 

def price ():
    price_excel = input("price excel:")
    number_of_article = input("Number:")
    taxes = float(input("taxes :"))
    price_incl = 0
    price_incl = (price_excel*number_of_article)*(1+(taxes))
    return price_incl

#Exercice 2

#Exercice 2.1

def deux_un(a,b):
    c = a
    a = b
    b = c
    
    return a , b

#Exerce 2.2

def deux_deux(a,b):
    a,b = b,a
    return a,b

#Exercice 2.3



#Exercice 3



def trois_variable ():  
    x = input("x=")
    y = input("y=")
    z = input("z=")
    x,y,z = y,z,x
    return x,y,z

#Exercice bonus

def paque (m):
    n = m - 1900
    a = n % 19
    b = (7*a+1) // 19
    c = (11*a -b + 4) % 29
    d = n // 4
    e = (n-c+d) % 7
    j = 31 + 25-c-e
    print("la date de mars est en")
