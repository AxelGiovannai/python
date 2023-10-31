list_test = [5,8,5,1,3,5,7,9,3,1] 

#Exercice 1

def occurence(x,list):
    c = 0
    for i in range(len(list)):
        if list[i] == x:
            c += 1
    return c

#Exercice 2

def recherche(x,list):
        c = False
        for i in range(len(list)):
            if list[i] == x:
                c = True
        return c

#Exercice 3        
        
def minimum(list):
    c = list[0]
    for i in range(len(list)):
         if c> list[i]:
              c = list[i]
    return c

#Exercice 4

def Index_Minimum(list):
     result = []
     c = minimum(list)
     for i in range(len(list)):
          if list[i] == c:
               result.append(i)
     return c,result


#Exercice 5 

def inversion(list):
    Reverse = []
    for i in range(len(list)):
         Reverse.insert(0,list[i])
    return Reverse

