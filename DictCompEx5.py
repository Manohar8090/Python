#DictCompEx5.py
oldempsal={100:1.2,200:2.3,300:4.5,400:0.5,500:6.0}
newempsal={eno:round(oldempsal[eno]+oldempsal.get(eno)*50/100,2)  for eno in oldempsal }
print("------------------------------------------------------------")
print("\tEmpno\t\tOld Salary\tNew Salary")
print("------------------------------------------------------------")
for eno in oldempsal:
	print("\t{}\t\t{}\t\t{}".format(eno,oldempsal.get(eno),newempsal.get(eno)))
print("------------------------------------------------------------")
