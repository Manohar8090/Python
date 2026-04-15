#Program for Demonstrating the Importance of Possitional Arguments
#PossArgsEx2.py
def  dispstudent(sno,sname,marks,crs):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("-"*50)
dispstudent(100,"RS",45.67,"PYTHON") # Function Call with Possitional Arguments
dispstudent(200,"TR",65.17,"PYTHON") # Function Call with Possitional Arguments
dispstudent(300,"DR",25.17,"PYTHON") # Function Call with Possitional Arguments
dispstudent(400,"SR",65.56,"PYTHON") # Function Call with Possitional Arguments
dispstudent(500,"JH",45.56,"PYTHON") # Function Call with Possitional Arguments
print("-"*50)
