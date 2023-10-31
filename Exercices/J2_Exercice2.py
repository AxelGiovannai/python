#Fibonacci

def Fibonacci():
   n = eval(input("U0 = "))
   a = 0
   b = 1
   c = 0
   print(a)
   print(b)
   for i in range(2,n):
       c = a + b
       a = b
       b = c
       c = 0
       print(b)
       


#Syracus

def Syracus():
    a = int(input("U0 = "))
    n = int(input("n terme = "))
    print(a)
    for i in range(1,n):
        if a%2==0:
            a=a/2
        else:
            a=3*a+1
        print(int(a))

#REVERSE SYRACUS !!!
