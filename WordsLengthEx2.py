#program for accepting List of Words and find their Length
#WordsLengthEx2.py
now=int(input("Enter How Many Words u Have:"))
if(now<=0):
    print("\t{} is Invalid Input".format(now))
else:
    lst=[]
    for i in range(1,now+1):
        word=input("Enter {} Word:".format(i))
        lst.append(word)
    else:
        print("List of Words")
        print(lst)
        print("---------------------------------")
        d={} # Empty Dict for Placing word as key and Its length as Value
        for word in lst:
            d[word]=len(word)
        for k,v in d.items():
            print("{}--->{}".format(k,v))
        print("---------------------------------")