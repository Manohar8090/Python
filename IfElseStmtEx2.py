#program for accepting a Numerical Value and Decide whether It is +VE OR -VE OR Zero
#IfElseStmtEx2.py
val=float(input("Enter Any Numerical Value:"))#10
if(val>0):
    print("\t{} is +VE".format(val))
else:
    if(val<0):
        print("\t{} is -VE".format(val))
    else:
        print("\t{} is ZERO".format(val))
    print("\tI am from inner-if-else Statement")
print("I am from Outer-if-else Statement ")
