#Program for Demonstrating the Need of  Keyword Variable Length Arguments
#PureKeywordVarLengthArgsEx4.py
def findtotal(sno,sname,cls,**submarks):
	print("="*50)
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Class:{}".format(cls))
	if(len(submarks)==0):pass
	else:
		totmarks=0
		for subject,marks in submarks.items():
			print("\t{}\t{}".format(subject,marks))
			totmarks+=marks
		print("-"*50)
		print("TOTAL MARKS={}".format(totmarks))
	print("-"*50)

#main program
findtotal(100,"Ramesh","X",English=80,Telugu=77,Hindi=89,Maths=99,Science=78,Social=80)
findtotal(200,"Rajesh","XI",Eng=89,Sanskrit=99,Maths=75,Physics=60,Chemistry=59)
findtotal(300,"Rakesh","B.Tech(CSE-With Knowledge)",OS=50,DBMS=45,NW=35)
findtotal(400,"Rossum","Research")
