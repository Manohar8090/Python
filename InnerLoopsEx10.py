#program for Deciding Primes  List of Ve Rabdom Numebrs
#InnerLoopsEx7.py
n=int(input("Enter Numbers u have:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("\tEnter Number for deciding prime or not {}:".format(i)))
        lst.append(val)
    else:
        print("List of Primes")
        for num in lst: # get the num from list object
            if(num<=1):
                continue
            res=True
            for i in range(2,num):
                if(num%i==0):
                    res=False
                    break
            if(res):
                print("\t{}".format(num))
