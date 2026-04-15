#Program for Demonstrating the Importance of Default Arguments
#DefaultArgsEx3.py
def  dispstudent(sno,sname,marks,crs="PYTHON",cnt="INDIA"): 
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE\tCOUNTRY")
print("-"*50)
dispstudent(100,"RS",45.67) # Function Call with Possitional Arguments
dispstudent(200,"TR",65.17) # Function Call with Possitional Arguments
dispstudent(300,"DR",25.17) # Function Call with Possitional Arguments
dispstudent(400,"SR",65.56) # Function Call with Possitional Arguments
dispstudent(500,"JH",45.56) # Function Call with Possitional Arguments
dispstudent(600,"DT",15.56,"HTML","USA") # Function Call with Possitional Arguments
dispstudent(700,"PT",35.56,cnt="RSA") # Function Call with Possitional Arguments with kyword arg
dispstudent(sname="KM",marks=11.11,cnt="NK",crs="C",sno=800,) # Function Call with  kyword arg
print("-"*50)
