#FunctionTest.py
def welcome(name): # Function Def
    print("Line:3:Hi:{}, Welcome to Functions".format(name))

if __name__=="__main__":
    print("I am from Main Program before function call")
    welcome("Rossum")
    print("I am from Main Program after function ")