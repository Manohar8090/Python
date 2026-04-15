#program for accepting a Value and Decide whether It is palindrome or not
#SimpleIfStmtEx1.py
value=input("Enter Any Value:")
if(value==value[::-1]):
    print("\t{} is Palindrome ".format(value))
if(value!=value[::-1]):
    print("\t{} is not Palindrome".format(value))
print("Program Execution Completed")