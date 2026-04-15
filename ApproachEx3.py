#Define a Function for cal addition of two Numbers
# INPUT         : Taking INPUT from Function Call
# PROCESS       : Doing the PROCESS in Function Body
# RESULT        : Displying the RESULT in Function Body
#ApproachEx3.py
def addop(k,v):
    r=k+v
    print("Sum({},{})={}".format(k,v,r))

#main Program
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
addop(a,b) # Function call

