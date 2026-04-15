#Program for Demonstrating the Need of  Keyword Variable Length Arguments
#PureKeywordVarLengthArgsEx7.py
def findtotal(sno,sname,cls,*intmarks, city="HYD",**submarks):
	print("="*50)
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Class:{}".format(cls))
	print("\tStudent City:{}".format(city))
	it=0
	print("\tStudent Internal Marks")
	for val in intmarks:
			print("\t\t{}".format(val))
			it=it+val
	print('\tExternal Marks')
	totmarks=0
	for subject,marks in submarks.items():
		print("\t{}\t{}".format(subject,marks))
		totmarks+=marks
	print("-"*50)
	print("TOTAL EXT MARKS={}\t INTERNAL MARKS={}".format(totmarks,it))
	print("\tTOTAL EXT+INTERNAL MARKS={}".format(totmarks+it))
	print("-"*50)

#main program
findtotal(100,"Ramesh","X",10,12,15,11,14,17,English=80,Telugu=77,Hindi=89,Maths=99,Science=78,Social=80)
findtotal(200,"Rajesh","XI",10,11,19,20,12,Eng=89,Sanskrit=99,Maths=75,Physics=60,Chemistry=59)
findtotal(300,"Rakesh","B.Tech(CSE-With Knowledge)",11,22,9,OS=50,DBMS=45,NW=35)
findtotal(400,"Rossum","Research",10,20,30,city="Dutch")
findtotal(500,"DT","POLITICS",Pol=22,Eco=18,geo=15,city="USA")
