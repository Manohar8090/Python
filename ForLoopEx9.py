#programming for Calculating sum of Squares and cubes of First N Natural Numbers,
#ForLoopEx9.py
n=int(input("Enter How Many Natural Number Sum u want:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("-"*50)
    print("Natural Numbers\t\tSquares\t\tCubes")
    print("-" * 50)
    s,ss,cs=0,0,0
    for i in range(1,n+1):
        print("\t\t{}\t\t\t\t{}\t\t{}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("-" * 50)
        print("\t\t{}\t\t\t\t{}\t\t{}".format(s, ss, cs))
        print("-" * 50)

