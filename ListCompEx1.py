#program for Getting List of +VE Elements.
#ListCompEx1.py
lst=[10,-20,30,-40,50,-15,-16,25,0,45]
pslist=[ val    for val  in lst   if val>0  ]  # List Comprehension
print("List of Given Values=",lst)
print("List of +VE Values=",pslist)