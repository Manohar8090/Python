#Define a Function for cal addition of two Numbers
# INPUT         : Taking INPUT from Function Call
# PROCESS       : Doing the PROCESS in Function Body
# RESULT        : Giving the RESULT Back to Function Call
#ApproachEx1.py
def addop(a,b):
    c=a+b
    return c

#main program
#Accept Two Numerical from KBD
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
c=addop(a,b) # Function call
print("Sum({},{})={}".format(a,b,c,))
print("-----------------------------------------")
k=float(input("Enter Value of K:"))
v=float(input("Enter Value of V:"))
r=addop(k,v) # Function call
print("Sum({},{})={}".format(k,v,r))
print("-----------------------------------------")