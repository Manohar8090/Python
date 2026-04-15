#Program for Demonstrating the need of Generators
#GenEx1.py
def kvrrange(Start,Stop):
	while(Start<=Stop):
		yield Start
		Start=Start+1

#main Program
r=kvrrange(1,5) # Function Call---return an object of <class, generator>
#To get the value from generator object, we use next()
for val in r:
	print(val)