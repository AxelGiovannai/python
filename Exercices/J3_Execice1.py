myList = [2, -3, ['xox', 69], 11]
myList
myList[-1]
myList[1] = 666
myList
myList[2][0][1]
myTuple = (2.718, 3.14, 1.414)
myTuple
myTuple[2]
myTuple[2] = 666
t = (7, -3, 2, 11, 666, -1975)
t[3:]
t[1:4]
t[1::2]
t[23]
l = [1,  2,  3,  4,  5]
l[2:4] = (6, 'x', 7)
l
l[1:6:2] = 'sup'
l
myList = list(range(1,10,2))
myList
yourList = list('The Rolling Stones')
yourList
myTuple = tuple(range(0,9,2))
myTuple
yourTuple = tuple('Tame Impala')
yourTuple
t = (7, -3, 2)
11 not in t
max(t)
tt = 2*t
tt
len(tt)
tt.count(-3)
tt.index(2)
tt.index(666)
l = (-2, 3, 11)

for x in l:
    print(x**2)

for i in range(len(l)):
    print("élément n°", i+1, ":", l[i]**2)

for i, x in enumerate(l):
    print("élément n°", i+1, ":", x**2)

m = 'Keith'

for x, y in zip(l,m):
    print(x, y)

myList = [1, 3, 5]
myList.append(7)
myList
myList.extend((8, 11))
myList
myList.remove(8)
myList.insert(4,9)
myList
myList.remove(666)

