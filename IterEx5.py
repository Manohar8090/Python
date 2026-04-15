#Program for Demonstrating the Need of Iterator
#IterEx5.py
x="PYTHON"
print("Content of x={}   Type={}".format(x,type(x)))
print("-------------------------------------------------------------------")
iterobj=iter(x) # Converting Iterable Object into Iterator Object
print("Type of Iterobj=",type(iterobj))
#To get the value from Iterator Object, we use next()
for val in iterobj:
	print(val)