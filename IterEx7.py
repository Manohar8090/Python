#Program for Demonstrating the Need of Iterator
#IterEx7.py
x=1000
print("Content of x={}   Type={}".format(x,type(x)))
print("-------------------------------------------------------------------")
iterobj=iter(x) 
print("Type of Iterobj=",type(iterobj))
#To get the value from Iterator Object, we use next()
for val in iterobj:
	print(val)

	