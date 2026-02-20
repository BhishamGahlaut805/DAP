#1.squares
def check(x):
    y = int(x**0.5)
    return y * y == x

res = list(filter(check, range(1, 101)))
print(res)

#1.Alt
def square(x):
    return x*x
num=range(1,11)
res1=list(map(square,num))
print(res1)

#2.EvenDelete
listNum=list(range(1,11))
for i in listNum:
    if i%2==0:
        listNum.remove(i)
print(listNum)

#3.20 odd numbers
listRes=[i for i in range(1,21) if i%2!=0]
print(listRes)
print([i for i in range(1,21) if i%2!=0])

#4.Filter
listN=[1,2,3,4,-1,-8,7,9,2,-1,-9,-8,8]
def checkN(x):
    return x>=0
listRes1=list(filter(checkN,listN))
print(listRes1)

#5.Median
listMed=[1,7,6,2,8]
def medianNum(l1):
    l1.sort()
    n=len(l1)
    if n%2==0:
        return (l1[n//2-1]+l1[n//2])/2
    else:
        return l1[n//2]
medianN=medianNum(listMed)
print(medianN)

#Output:

'''
PS C:\Users\bhish\OneDrive\Desktop\DAP> python -u "c:\Users\bhish\OneDrive\Desktop\DAP\3__List__Tuple.py"
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[1, 3, 5, 7, 9]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
[1, 2, 3, 4, 7, 9, 2, 8]
6
PS C:\Users\bhish\OneDrive\Desktop\DAP> 
'''