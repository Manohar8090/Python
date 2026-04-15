#Program for Reading the Data from the File by using readlines()
#FileReadEx2.py
def fileread():
    print("------------------------------------------")
    with open("student1.data","r") as fp:
        filedata=fp.readlines()
        for val in filedata:
            print(val,end="")
    print("------------------------------------------")

#main program
fileread()