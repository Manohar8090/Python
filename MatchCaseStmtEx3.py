#MatchCaseStmtEx3.py
import sys

s="""--------------------------------------------------------------
						Base Conversion Calculator
--------------------------------------------------------------
        I.  Decimal to Binary
            Decimal to Octal
            Decimal to Hexa
        II. Binary to Decimal
            Binary to octal
            Binary to Hexa
        III. Octal to Decimal
             Octal to Binary
             Octal to Hexa
        IV. Hexa to Decimal
            Hexa  to Binary
            Hexa to Octal
        V: Exit
--------------------------------------------------------------------"""
print(s)
ch=input("Enter your choice: ")
match(ch):
   case "I":
       dv=int(input("Enter Integer Values for Converting into Binary,Octal and Hexa: "))
       print("\tGiven Decimal Value={}".format(dv))
       print("\tBin({})={}".format(dv,bin(dv)))
       print("\tOct({})={}".format(dv, oct(dv)))
       print("\tHex({})={}".format(dv, hex(dv)))

   case "II":
       bv = input("Enter Binary Value Preceded with 0b or 0B for Converting into Dec,Octal and Hexa:")
       print("\tGiven Binary Value={}".format(bv))
       x=int(bv,2)
       print("\tDec({})={}".format(bv, x))
       print("\tOct({})={}".format(bv, oct(x)))
       print("\tHex({})={}".format(bv, hex(x)))
   case "III":
       ov = input("Enter Octal Value Preceded with 0o or 0O for Converting into Dec,Binary and Hexa:")
       print("\tGiven Octal Value={}".format(ov))
       x = int(ov, 8)
       print("\tDec({})={}".format(ov, x))
       print("\tBin({})={}".format(ov, bin(x)))
       print("\tHex({})={}".format(ov, hex(x)))
   case "IV":
       hv = input("Enter Hexa Dec Value Preceded with 0x or 0X for Converting into Dec,Bin and Oct:")
       print("\tGiven Hexa Dec Value={}".format(hv))
       x = int(hv, 16)
       print("\tDec({})={}".format(hv, x))
       print("\tBin({})={}".format(hv, bin(x)))
       print("\tOct({})={}".format(hv, oct(x)))
   case "V":
       print("\tThx for using Program")
       sys.exit()
   case _:
        print("\tUr Selection of Operation is wrong-try again")



