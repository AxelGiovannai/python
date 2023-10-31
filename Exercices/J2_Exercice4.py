import random

def saisie_joueur():
    joueur = int(input("Combien prenez vous d allumettes ? "))
    if 1<=joueur<=3 and joueur<board :
        return joueur
    else:
        print("Le nombre d'allumette doit etre entre 1 et 3. ")
        saisie_joueur()

def Nombre_allumette(): # 1
    init =  int(input("Avec combien d'allumettes jouez_vous : "))
    if init%2!=0 and init>0:
        return init
    else:
        print("Le nombre d'allumette doit etre impair ou superieur a zero.")
        Nombre_allumette()

def Ordinateur(board):
    ordi = random.randint(1,board)
    if ordi%2!=0:
        return ordi
    else:
        Ordinateur(board)

def board():
    