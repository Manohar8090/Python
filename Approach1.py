#Define a Function for cal addition of two Numbers
#Approach1.py
def addop(a,b): # here a,b, are called formal params
    c=a+b # here c is called Local Variables
    return c

#Main Program
print("I am from Main Program after function Definition before function call")
res=addop(100,200) # Function call
print("Sum=",res)
c=addop(-100,-20) # Function call
print("Sum=",c)
print("I am from Main Program after function execution ")