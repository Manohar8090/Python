#program for accepting List of Words and find their Length
#WordsLengthEx1.py
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
        for word in lst:
            print("\t{}--->{}".format(word,len(word)))
        print("---------------------------------")