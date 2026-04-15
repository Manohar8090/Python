#Program for Demonstrating How to write the Data to the File
#FileWriteEx1.py
sno=400
sname="Jhon"
marks=86.57 # here sno,sname,marks are Objects Present in Main Memory.
with open("student1.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data Written to the File")
