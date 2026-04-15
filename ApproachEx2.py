#Define a Function for cal addition of two Numbers
# INPUT         : Taking the INPUT in Function Body
# PROCESS       : Doing the PROCESS in Function Body
# RESULT        : Displying the RESULT in Function Body
#ApproachEx2.py
def addop():
    #taking the input in Function body
    a = float(input("Enter Value of a:"))
    b = float(input("Enter Value of b:"))
    #process
    c=a+b
    #display the result
    print("Sum({},{})={}".format(a,b,c,))

#Main Program
addop() # Function Call
