#Program for Demonstrating the need of Generators
#GenEx2.py
def kvrrange(Value):
	Start=0
	while(Start<=Value):
		yield Start
		Start=Start+1

#main Program
r=kvrrange(6) # Function Call---return an object of <class, generator>
#to get the value from generator object, we use next()
print(next(r))
print(next(r))
print(next(r))
for val in r:
	print("\t{}".format(val))