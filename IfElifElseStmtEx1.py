#program for accepting a Value and Decide whether It is palindrome or not
#IfElifElseStmtEx1.py
# value=input("Enter Any Value:")
# if(value==value[::-1]):
#     print("\t{} is Palindrome ".format(value))
# elif (value != value[::-1]):
#     print("\t{} is not Palindrome".format(value))
# print("Program Execution Completed")

value=input("Enter Any Value:")
if(value==value[::-1]):
    print("\t{} is Palindrone ".format(value))
elif (value != value[::-1]):
    print("\t{} is not Palindrome".format(value))
print("Program Execution Completed")