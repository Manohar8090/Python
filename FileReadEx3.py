#program for accepting any file name and display Its content
#FileReadEx3.py
def dispfilecontent():
    try:
        filename=input("Enter Any File Name:")
        with open(filename,"r") as fp:
            filedata=fp.read()
            print("--------------------------------------")
            if(len(filedata)>0):
                print(filedata)
            else:
                print("File does not contain Data")
            print("--------------------------------------")
    except FileNotFoundError:
        print("File Does not exist")

#Main Program
dispfilecontent()