#Program for Reading the Data from the File by using read()
#FileReadEx1.py
def fileread():
    try:
        with open("student1.data","r") as fp:
            filedata=fp.read()
            print("----------------------------------")
            print(filedata)
            print("----------------------------------")
    except FileNotFoundError:
        print("File Does not exist")
#main Program
fileread()