#Program for accepting Two Numerical Values and
# Find Biggest among them and check for equality without using max()
#AnonymousFunEx2.py

findmax=lambda k,v: k if k>v else v if v>k else "Both Values are equal"

#main Program
print("Enter two Numerical Values")
a,b=float(input()),float(input())
bv=findmax(a,b) # Anonymous function
print("Max({},{})={}".format(a,b,bv))
