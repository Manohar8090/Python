#Program for cal simple interest and total amount to pay
#DataReadEx9.py
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of interest:"))
#cal si
si=(p*t*r)/100
#cal totamt
totamt=p+si
print("*"*40)
print("\tPrinciple Amount:",p)
print("\tTime:",t)
print("\tRate of interest:",r)
print("\tSimple Interest:",si)
print("\tTotal Amount:",totamt)
print("*"*40)

