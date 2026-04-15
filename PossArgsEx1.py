#Program for Demonstrating the Importance of Possitional Arguments
#PossArgsEx1.py
def  dispstudent(sno,sname,marks):
	print("\t{}\t{}\t{}".format(sno,sname,marks))

#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS")
print("-"*50)
dispstudent(100,"RS",45.67) # Function Call with Possitional Arguments
dispstudent(200,"TR",65.17) # Function Call with Possitional Arguments
dispstudent(300,"DR",25.17) # Function Call with Possitional Arguments
dispstudent(400,"SR",65.56) # Function Call with Possitional Arguments
dispstudent(marks=55.55,sno=400,sname="KV") # Function Call--with Keyword args
dispstudent(500,marks=56.23,sname="JH")  # Function Call with Possitional Arguments and  Keyword args
#dispstudent(marks=16.23,sname="JG",600) --SyntaxError: positional argument follows keyword argument
print("-"*50)
