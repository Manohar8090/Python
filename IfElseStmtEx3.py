#program for accepting a Numerical Value and Decide whether It is Even or Odd
#IfElseStmtEx3.py
value=float(input("Enter Any Numerical Value:"))
if(value>0) and (value%2==0):
    print("\t{} is +VE EVEN".format(value))
else:
    if (value > 0) and (value % 2 != 0):
        print("\t{} is +VE ODD".format(value))
    else:
        print("\t{} is Invalid input".format(value))
print("Program execution Completed")
