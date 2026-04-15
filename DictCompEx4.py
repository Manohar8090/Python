#Program for Reading the Values from KeyBoard  and find Sqr and sqrt by using Comprehension Concept
#DictCompEx4.py
print("Enter List of Values Separated by Space:")
lst=[  float(val)       for val in input().split()     ]  # List Comprehension
print("Given List of Values:{}".format(lst))
sqrvals={val:val**2   for val in lst}
sqrtvals={val:val**0.5 for val in lst}
print("----------------------------------------------------")
print("Given Value\tSquarevalue")
print("----------------------------------------------------")
for k,v in sqrvals.items():
	print("\t{}\t{}".format(k,v))
print("----------------------------------------------------")
print("Given Value\tSquare Root Value")
print("----------------------------------------------------")
for k,v in sqrtvals.items():
	print("\t{}\t{}".format(k,v))
print("------------------------------------------------------------")
print("Given Value\tSquare  Value\tSquare Root Value")
print("------------------------------------------------------------")
for k,v in sqrvals.items():
	print("\t{}\t{}\t\t{}".format(k,v,round(sqrtvals[k],2)))
print("------------------------------------------------------------")