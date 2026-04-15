#Program for accepting Two Numerical Values and
# Find Biggest among them by using max()
#AnonymousFunEx3.py

findmax=lambda k,v: max(k,v)

#main Program
print("Enter two Numerical Values")
a,b=float(input()),float(input())
bv=findmax(a,b) # Anonymous function
print("Max({},{})={}".format(a,b,bv))