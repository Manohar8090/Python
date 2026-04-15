#program for Finding Finding Square for Every Value of list
#DictCompEx3.py
vals=[12,4,6,18,3,19]
sqrvals={Val: Val**2    for Val in vals} # Dict Comprehension
for k,v in sqrvals.items():
	print("\t{}--->{}".format(k,v))
