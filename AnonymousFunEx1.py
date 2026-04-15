#Anonymous functions for cal Diff Arithmetic Operations
#AnonymousFunEx1.py
import sys
sumop=lambda a,b: a+b
subop=lambda a,b: a-b
mulop=lambda a,b: a*b
divop=lambda a,b: a/b
floordivop=lambda a,b: a//b
modop=lambda a,b: a%b
expop=lambda a,b: a**b
#Main Program
while(True):
    print("-"*50)
    print("\tArithmetic Operations")
    print("-"*50)
    print("\t\t1. Addition")
    print("\t\t2. Substraction")
    print("\t\t3. Multiplication")
    print("\t\t4. Division")
    print("\t\t5. Floor Division")
    print("\t\t6. Modulo Division")
    print("\t\t7. Expoentiation")
    print("\t\t8. Exit")
    print("-"*50)
    ch=int(input("Enter your choice:"))
    match(ch):
        case 1:
            print("Enter two Values for addition")
            a,b=float(input()),float(input())
            res=sumop(a,b) # Anonymous Function Call
            print("Sum({},{})={}".format(a,b,res))
        case 2:
            print("Enter two Values for SubStraction")
            a, b = float(input()), float(input())
            res = subop(a, b)  # Anonymous Function Call
            print("Sub({},{})={}".format(a, b, res))
        case 3:
            print("Enter two Values for Multiplication")
            a, b = float(input()), float(input())
            res = mulop(a, b)  # Anonymous Function Call
            print("Mul({},{})={}".format(a, b, res))
        case 4:
            print("Enter two Values for Division")
            a, b = float(input()), float(input())
            res = divop(a, b)  # Anonymous Function Call
            print("Div({},{})={}".format(a, b, res))
        case 5:
            print("Enter two Values for Floor Division")
            a, b = float(input()), float(input())
            res = floordivop(a, b)  # Anonymous Function Call
            print("FloorDiv({},{})={}".format(a, b, res))
        case 6:
            print("Enter two Values for Modulo Division")
            a, b = float(input()), float(input())
            res = modop(a, b)  # Anonymous Function Call
            print("Mod({},{})={}".format(a, b, res))
        case 7:
            a, b = float(input("Enter Base:")), float(input("Enter Power:"))
            res = expop(a, b)  # Anonymous Function Call
            print("Pow({},{})={}".format(a, b, res))
        case 8:
            print("Thx for Using System")
            sys.exit()
        case _:
            print("Ur Selection of operation is wrong-try again")