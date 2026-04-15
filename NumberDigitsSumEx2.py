#program for Finding Sum of Digits of Given Number--logic-2
#NumberDigitsSumEx2.py
num=int(input("Enter Any Integer Number:"))
print("\tGiven Number={}".format(num)) # 3489
tn=num
s=0
while(num>0):
    d=num%10
    s=s+d
    num=num//10
else:
    print("\tSumOfDigist({})={}".format(tn,s))



