#Program for Demonstrating the need of Closure.
#ClosureEx4.py
def  welcome(sname): # Outer Function
	print("I am from Outer function")
	def greet(pname):  # inner Function
		print("'{}''is welcoming to '{}'".format(pname,sname))
	greet("Ramesh")
	greet("Rakesh")
	greet("Raj")

	

#Main Program
welcome("Rossum")
