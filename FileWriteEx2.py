#Program for Demonstrating How to write the Data to the File
#FileWriteEx2.py
print('--------------------------------------')
sno=int(input("Enter Student Number:"))
sname=input("Enter Student Name:")
marks=float(input("Enter Student Marks:")) # here sno,sname,marks are Objects Present in Main Memory.
print('--------------------------------------')
with open("student1.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data Written to the File")
