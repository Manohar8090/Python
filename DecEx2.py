#DecEx2.py--Model-2
def square(gv):
	def calsqr():
		n=gv()
		res=n**2
		return n,res
	return calsqr

@square   
def getval(): # Thif Function Def by KVR
	return float(input("Enter Any Numerical Value:"))

#Main Program
num,result=getval() # Normal Function call
print("Square({})={}".format(num,result))