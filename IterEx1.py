#Program for Demonstrating the Need of Iterator
#IterEx1.py
x=[10,20,30,40,50,"Python",True,2+3j]
print("Content of x={}   Type={}".format(x,type(x)))
print("-------------------------------------------------------------------")
iterobj=iter(x) # Converting Iterable Object into Iterator Object
print("Type of Iterobj=",type(iterobj))
#To get the value from Iterator Object, we use next()
print(next(iterobj))
print(next(iterobj))
for val in iterobj:
	print(val)
