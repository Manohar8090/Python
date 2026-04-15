#DecEx3.py--Model-2
def squareroot(csqrt):
	def calsqrtval():
		n,sqrv=csqrt()
		sqrtv=n**0.5
		return n,sqrv,sqrtv
	return calsqrtval

def square(gv):
	def calsqr():
		n=gv()
		res=n**2
		return n,res
	return calsqr

@squareroot
@square   
def getval(): # Thif Function Def by KVR
	return float(input("Enter Any Numerical Value:"))

#Main Program
num,sqrresult,sqrtresult=getval() # Normal Function call
print("Square({})={}".format(num,sqrresult))
print("SquareRoot({})={}".format(num,sqrtresult))