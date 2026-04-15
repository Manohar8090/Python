#program for accepting a Numerical Value and Decide whether It is +VE OR -VE OR Zero
#SimpleIfStmtEx2.py
val=float(input("Enter Any Numerical Value:"))
if(val>0):
    print("\t{} is +VE".format(val))
if(val<0):
    print("\t{} is -VE".format(val))
if(val==0):
    print("\t{} is ZERO".format(val))
print("Program execution is completed")

