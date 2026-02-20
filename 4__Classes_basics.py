#Program-1 Marks and total of 3 subjects marks
class student:
    def __init__(self,mark1,mark2,mark3):
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def total(self):
        totalMarks=self.mark1+self.mark2+self.mark3
        print("Total Marks are : ",totalMarks)
s1=student(98,78,94)
s1.total()

#-----------------------------------------------------------------------------------------

#Program 2 :area,CircumFerence

class circle:
    pi=3.14
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        totalArea=circle.pi*self.rad*self.rad
        print("Area of circle with radius ",self.rad," is ",totalArea)
    def circumference(self):
        totalCircum=circle.pi*2*self.rad
        print("CircumFerence of circle with radius ",self.rad," is ",totalCircum)

c1=circle(7)
c1.area()
c1.circumference()

#-------------------------------------------------------------------------------------------


#3.LARGEST number in a list

class check:
    def __init__(self,numList):
        self.numList=numList
    def find(self):
        largest=self.numList[0]
        for i in range(1,len(self.numList)):
            if self.numList[i]>largest:
                largest=self.numList[i]
        print("The Largest Number in the List is : ",largest)
c2=check([1,6,7,8,9,5,32])
c2.find()

#-----------------------------------------------------------------------------


#4.Bank Account

class account:
    def __init__(self):
        self.balance=0
    def displayBalance(self):
        print("The Current Account Balance is : ",self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print("Amount ",amount," deposited Successfully")
        account.displayBalance(self)
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient Balance")
        print("Amount ",amount," withdrawn Successfully")
        account.displayBalance(self)
a1=account()
a1.displayBalance()
a1.deposit(50000)
a1.withdraw(23400)

#-------------------------------------------------------------------------------------------------

#using exception handling
#1.Program-1
#Program-1 Marks and total of 3 subjects marks
class studentNew:
    def __init__(self,mark1,mark2,mark3):
        try:
            for mark in(mark1,mark2,mark3):
                if not(mark>=0 and mark<=100):
                    raise ValueError("Marks should be Between 0 and 100")

            self.mark1=mark1
            self.mark2=mark2
            self.mark3=mark3
        except ValueError as e:
            print("Error : ",e)
            raise

    def total(self):
        totalMarks=self.mark1+self.mark2+self.mark3
        print("Total Marks are : ",totalMarks)

try:
    s2=studentNew(98,78,94)
    s2.total()
except Exception:
    print("Unknown Exception has occured")
    raise

#------------------------------------------------------------------------

#Program2:Area of Circle with exception handing

class circle1:
    pi=3.14
    def __init__(self,rad):
        try:
            self.rad=rad
        except ValueError as e :
            print("Error : ",e)
            raise
    def area(self):
        totalArea=circle.pi*self.rad*self.rad
        print("Area of circle with radius ",self.rad," is ",totalArea)
    def circumference(self):
        totalCircum=circle.pi*2*self.rad
        print("CircumFerence of circle with radius ",self.rad," is ",totalCircum)

c1=circle1(7)
c1.area()
c1.circumference()

#---------------------------------------------------------------------------------------------------
#Output:
'''
PS C:\Users\bhish\OneDrive\Desktop\DAP> python -u "c:\Users\bhish\OneDrive\Desktop\DAP\4__Classes_basics.py"
Total Marks are :  270
Area of circle with radius  7  is  153.86
CircumFerence of circle with radius  7  is  43.96
The Largest Number in the List is :  32
The Current Account Balance is :  0
Amount  50000  deposited Successfully
The Current Account Balance is :  50000
Amount  23400  withdrawn Successfully
The Current Account Balance is :  26600
Total Marks are :  270
Area of circle with radius  7  is  153.86
CircumFerence of circle with radius  7  is  43.96
PS C:\Users\bhish\OneDrive\Desktop\DAP>

'''