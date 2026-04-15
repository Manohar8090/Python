#VoterEx2.py
while(True):
    age=int(input("Enter Ur Correct Age:"))
    if(age>=18) and (age<=100):
        print("UR Age:{} and Eligible to Vote:".format(age))
        break
    else:
        print("\t{} Years Citizen is Not Eligible Vote".format(age))

