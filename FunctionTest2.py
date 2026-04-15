#FunctionTest.py
def welcome(name): # Function Def
    print("Line:3:Hi:{}, Welcome to Functions".format(name))

#Main Program
print("I am from Main Program before function call")
welcome("Rossum") # Function Call
welcome("Travis") # Function Call
print("I am from Main Program after function ")
