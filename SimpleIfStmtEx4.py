#program for accepting a P,T,R Values and Cal simple interest
#SimpleIfStmtEx4.py
p=float(input("Enter Principle Amount:")) # p=-1000
t=float(input("Enter Time :")) # t=3
r=float(input("Enter Rate of Interest :")) #r=4
if(p>0) and (t>0) and (r>0):
    si=(p*t*r)/100
    print("\tSimple Interest={}".format(si))
if(p<=0):
    print("\tDon't enter -Ve/zero for principle amount")
if(t<=0):
    print("\tDon't enter -Ve/zero for Time")
if(r<=0):
    print("\tDon't enter -Ve/zero for rate of interest")




