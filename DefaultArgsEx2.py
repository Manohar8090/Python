#Program for Demonstrating the Importance of Default Arguments
#DefaultArgsEx2.py
def  dispstudent(sno,sname,marks,crs="PYTHON"): # here crs="PYTHOn is called default Parameter
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("-"*50)
dispstudent(100,"RS",45.67) # Function Call with Possitional Arguments
dispstudent(200,"TR",65.17) # Function Call with Possitional Arguments
dispstudent(300,"DR",25.17) # Function Call with Possitional Arguments
dispstudent(400,"SR",65.56) # Function Call with Possitional Arguments
dispstudent(500,"JH",45.56) # Function Call with Possitional Arguments
dispstudent(600,"DT",15.56,"HTML") # Function Call with Possitional Arguments
dispstudent(700,"PT",35.56) # Function Call with Possitional Arguments
print("-"*50)
