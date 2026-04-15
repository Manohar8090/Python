#StudentMarksReportEx1.py
#Data Validation for accepting sno:
while(True):
    sno=int(input("Enter Student Number(100-200):"))
    if(sno>=100) and (sno<=200):
        break
    print("\t{} is Invalid Student Number".format(sno))
#Data Validation for accepting sname:
while(True):
    res = True
    sname=input("Enter UR Name:") # Guido Va2n Rossum
    if(sname.isspace()):
        print("\tDon't enter space for name-try again")
    elif(len(sname)==0):
        print("\tU Must Enter Ur name-try again")
    else:
        words=sname.split() # words=[Guido,Va2n, Rossum]
        for word in words:
            if(not word.isalpha()):
                res=False
                break
        if(res):
            sname=" ".join(words)
            break
        print("\t{} is invalid Name -try again".format(sname))
#Data Validation for Marks in C-100
while(True):
    cm=input("Enter Marks in C Lang:")
    if(cm.isdigit()):
        if int(cm) in range(0,101):
            break
    print("\t{} Invalid Marks in C Lang".format(cm))

#Data Validation for Marks in CPP-100
while(True):
    cppm=input("Enter Marks in C++ Lang:")
    if(cppm.isdigit()):
        if int(cppm) in range(0,101):
            break
    print("\t{} Invalid Marks in C++ Lang".format(cppm))

#Data Validation for Marks in Python-100
while(True):
    pym=input("Enter Marks in PYTHON Lang:")
    if(pym.isdigit()):
        if int(pym) in range(0,101):
            break
    print("\t{} Invalid Marks in C++ Lang".format(pym))
#Cal tootal marks
totmarks=int(cm)+int(cppm)+int(pym)
percent=(totmarks/300)*100
#If Any Student gets Less than 40 in any of the subject then given Grade=FAIL
if(int(cm)<40) or  (int(cppm)<40) or (int(pym)<40):
    grade="FAIL"
else:
    if(totmarks in range(250,301)):
        grade="DITNCTION"
    elif (200<=totmarks<=249):
        grade = "FIRST"
    elif (totmarks>=150) and (totmarks<=199):
        grade = "SECOND"
    elif (totmarks in range(120,150)):
        grade = "THIRD"
#Display Student Marks Report.
print("*"*50)
print("\t\tStudent Marks Report")
print("*"*50)
print("\t\tStudent Number:{}".format(sno))
print("\t\tStudent Name:{}".format(sname))
print("\t\tStudent Marks in C:{}".format(cm))
print("\t\tStudent Marks in C++:{}".format(cppm))
print("\t\tStudent Marks in PYTHON:{}".format(pym))
print("\t\tStudent Total Marks:{}".format(totmarks))
print("\t\tStudent Percentage of Marks:{}".format(percent))
print("\t\tStudent Grade:{}".format(grade))
print("*"*50)










