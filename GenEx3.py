#Program for Demonstrating the need of Generators
#GenEx3.py
def kvrrange(Start,Stop,Step):
	while(Start<Stop):
		yield Start
		Start=Start+Step

#main Program
r=kvrrange(10,21,2) # Function Call---return an object of <class, generator>
#to get the value from generator object, we use next()
for val in r:
	print(val)
print("----------------------------------------------------------")
r1=kvrrange(100,151,10) # Function Call---return an object of <class, generator>
#to get the value from generator object, we use next()
for val in r1:
	print(val)