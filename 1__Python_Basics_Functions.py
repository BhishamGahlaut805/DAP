#1.Check is_Prime
def is_Prime(val):
    if(val<=1):
        print(val," is not a Prime Number")
    primeNo=True

    for i in range (2,int(val**0.5)+1):
        if(val%i==0):
            primeNo=False
            break
    if primeNo:
        print(val," is a Prime Number")
    else:
        print(val," is not a Prime Number")

#num=int(input("Enter a Number to Check : "))
#is_Prime(num)

#2.Read marks of 10 students

print("Enter Marks of 10 students : ")
marks_list=[]

for i in range (1,11):
    marks1=float(input())
    marks_list.append(marks1)

for i in range (0,len(marks_list)):
    marks1=marks_list[i]
    if marks1>=50:
        print("Student ",i+1," Passed having Marks = ",marks_list[i])
    else:
        print("Student ",i+1," Failed having Marks = ",marks_list[i])

#Output

'''
Enter Marks of 10 students :
34
45
32
12
57
78
67
5
44
34
Student  1  Failed having Marks =  34.0
Student  2  Failed having Marks =  45.0
Student  3  Failed having Marks =  32.0
Student  4  Failed having Marks =  12.0
Student  5  Passed having Marks =  57.0
Student  6  Passed having Marks =  78.0
Student  7  Passed having Marks =  67.0
Student  8  Failed having Marks =  5.0
Student  9  Failed having Marks =  44.0
Student  10  Failed having Marks =  34.0
PS C:\Users\bhish\OneDrive\Desktop\DAP> 
'''