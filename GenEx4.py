#Program for Demonstrating the need of Generators
#GenEx4.py
def kvrrange(Start,Stop=1,Step=1):
	if(Start>Stop):
		Stop=Start
		Start=1
	while(Start<=Stop):
		yield Start
		Start=Start+Step

#Main Program
r1=kvrrange(6) # Function Call
for val in r1:
	print(val)
print("--------------------------------------------------")
r2=kvrrange(100,106)
for val in r2:
	print(val)
print("--------------------------------------------------")
r3=kvrrange(100,151,10)
for val in r3:
	print(val)