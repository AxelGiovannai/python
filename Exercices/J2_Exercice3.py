def SaisirLaBorneSuperieur():
   a = int(input("La borne superieur : "))
   return a

def EstUnDiviseur(nombre,diviseur):
    bool = False
    if nombre % diviseur == 0:
       bool=True
    else:
        bool=False
    return bool

def SommeDesDiviseurs(nombre):
    c = 0
    for i in range(1,int(nombre)):
        if EstUnDiviseur(nombre,i)==True:
            c += i
        else:
            c 
    return c

def EstParfait(nombre):
    c = SommeDesDiviseurs(nombre)
    bool = False
    if c == nombre:
        bool = True
    else:
        bool = False
    return bool

def AffichersNombreParfaitsJusqua(nombre):
    for i in range(1,nombre+1):
        bool = EstParfait(i)
        if bool == False:
            pass
        else:
            print(i)   

def NombresParfaits():
    nombre = SaisirLaBorneSuperieur()
    AffichersNombreParfaitsJusqua(nombre)


