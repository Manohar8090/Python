#DecEx4.py--Model-2
def cube(calsqrtval):
	def calcube():
		n,sqrval,sqrtval=calsqrtval()
		cbval=n**3
		return n,sqrval,sqrtval,cbval
	return calcube

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

@cube
@squareroot
@square   
def getval(): # Thif Function Def by KVR
	return float(input("Enter Any Numerical Value:"))

#Main Program
num,sqrresult,sqrtresult,cbv=getval() # Normal Function call
print("Square({})={}".format(num,sqrresult))
print("SquareRoot({})={}".format(num,sqrtresult))
print("Cube({})={}".format(num,cbv))