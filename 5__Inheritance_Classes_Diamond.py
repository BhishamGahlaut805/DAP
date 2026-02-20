#Inheritance in Python(OOP)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)

class teacher(person):
    def __init__(self, name, age,exp,rArea):
        super().__init__(name, age)
        self.exp=exp
        self.rArea=rArea
t1=teacher("Dr HM",30,5,"Mathematics-Calculus and Linear Algebra")
t1.display()

#-----------------------------------------------------------------------------------------------
class Student:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name :", self.name)


class AcadPerformance(Student):
    def __init__(self, name):
        super().__init__(name)

    def AcadScore(self):
        print("Academic Score: 90% and Above")


class ECA(Student):
    def __init__(self, name):
        super().__init__(name)

    def ECA_Score(self):
        print("ECA Score: 65% and Above")


class Result(AcadPerformance, ECA):
    def __init__(self, name):
        super().__init__(name)   # follows MRO

    def eligibility(self):
        self.show_name()
        self.AcadScore()
        self.ECA_Score()


r = Result("Amit")
r.eligibility()

print(Result.mro())

#-----------------------------------------------------------------------------------------------------
#Exception Handling
num=int(input("Enter the numerator"))
den=int(input("Enter the Denominator"))
try:
    quotient=num/den
    print("The Quotient is ",int(quotient))
except ZeroDivisionError:
    print("Cannot Divide by 0 ")
except FileNotFoundError:
    print("File not found")
except ArithmeticError:
    print("Arithmetic Error")
except Exception:
    print("Unknown Exception Caught")

#---------------------------------------------------------------------

#Output
'''
PS C:\Users\bhish\OneDrive\Desktop\DAP> python -u "c:\Users\bhish\OneDrive\Desktop\DAP\5__Inheritance_Classes_Diamond.py"
Dr HM
30
Name : Amit
Academic Score: 90% and Above
ECA Score: 65% and Above
[<class '__main__.Result'>, <class '__main__.AcadPerformance'>, <class '__main__.ECA'>, <class '__main__.Student'>, <class 'object'>]
Enter the numerator3
Enter the Denominator0
Cannot Divide by 0
PS C:\Users\bhish\OneDrive\Desktop\DAP> 
'''