#Program for Demonstrating the Need of Iterator
#IterEx4.py
x={1:"Python",2:"C++",3:"C",4:"Java"}
print("Content of x={}   Type={}".format(x,type(x)))
print("-------------------------------------------------------------------")
iterobj=iter(x) # Converting Iterable Object into Iterator Object
print("Type of Iterobj=",type(iterobj))
#To get the value from Iterator Object, we use next()
for Key in iterobj:
	print(Key,"--->",x[Key])