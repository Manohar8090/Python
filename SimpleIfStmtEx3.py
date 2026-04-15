#program for accepting a Numerical Value and Decide whether It is Even or Odd
#SimpleIfStmtEx3.py
value=float(input("Enter Any Numerical Value:"))
if(value>0) and (value%2==0):
    print("\t{} is EVEN".format(value))
if(value>0) and (value%2!=0):
    print("\t{} is ODD".format(value))
if(value<0):
    print("\t{} is Invalid input".format(value))
print("Program execution Completed")
