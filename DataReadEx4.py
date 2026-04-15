#Program for accepting two Numerical Values and find their Product
#DataReadEx4.py
print("Enter Two Numerical Values")
x=input()
y=input()
#convert x and y values in int type
a=float(x)
b=float(y)
#find product
c=a*b
#display the result
print("-"*50)
print("Product({},{})={}".format(a,b,c))
print("-------------------OR------------------")
print("Product(%0.2f,%0.2f)=%0.2f" %(a,b,c))
print("-------------------OR------------------")
print("Product({},{})={}".format(round(a,2),round(b,2),round(c,2) ))
print("-"*50)