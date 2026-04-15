#DecEx1.py--Model-1
def square(kvr):# decorator Def
	def calculations():
		n=kvr()
		res=n**2
		return n,res
	return calculations


def getval(): # Thif Function Def by KVR
	return 5

#Main Program
calc=square(getval) # Fucntion Call takes Normal Function Name as argument--Decorator
n,res=calc()
print("Square({})={}".format(n,res))