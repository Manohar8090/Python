#program for Finding Sum of Digits of Given Number--logic-1
#NumberDigitsSumEx1.py
num=int(input("Enter Any Integer Number:"))
print("\tGiven Number={}".format(num)) # 3489
s=0
for d in str(num):
    s=s+int(d)
else:
    print("\tDigitsSum({})={}".format(num,s))



