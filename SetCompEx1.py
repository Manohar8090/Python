#program for Getting List of +VE Elements.
#SetCompEx1.py
lst=[10,-20,30,-40,50,-15,-16,25,0,45]
possetvals={ val    for val  in lst   if val>0  }  # set Comprehension
negsetvals={ val    for val  in lst   if val<0  }  # set Comprehension
print("List of Given Values=",lst)
print("List of +VE Values=",possetvals)
print("List of -VE Values=",negsetvals)