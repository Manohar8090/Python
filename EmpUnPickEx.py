#Program for Reading the Records from File where It Contains Employee  Records(emp.pick)
#EmpUnPickEx.py
import pickle
with open("emp.pick","rb") as fp:
	print("---------------------------------------------------------------")
	while(True):
		try:
			record=pickle.load(fp)
			for val in record:
				print("\t{}".format(val),end="  ")
			print()
		except EOFError:
			print("---------------------------------------------------------------")
			break

