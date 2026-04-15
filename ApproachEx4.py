#Define a Function for cal addition of two Numbers
# INPUT         : Taking the INPUT in Function Body
# PROCESS       : Doing the PROCESS in Function Body
# RESULT        : Giving the RESULT Back to Function Call
#ApproachEx4.py
def addop():
    a=float(input("Enter Value of a:"))
    b=float(input("Enter Value of b:"))
    c = a+b
    return a,b,c # here return statement can return One or more number of Values
#Main Program
x,y,res=addop() # Fucntion Call with Multi line assignment
print("Sum({},{})={}".format(x,y,res))
print("--------------------OR-------------------------")
kvr=addop() # Function call with single assignment
print("Sum({},{})={}".format(kvr[0],kvr[1],kvr[2]))
print("Sum({},{})={}".format(kvr[-3],kvr[-2],kvr[-1]))
