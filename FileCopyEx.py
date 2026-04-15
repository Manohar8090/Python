#program for Copying the content of one file into another File
#FileCopyEx.py
def filecopy():
    try:
        srcfile=input("Enter Source File:")
        with open(srcfile,"r") as rp:
            dstfile=input("Enter Destination File:")
            with open(dstfile,"a") as wp:
                srcfiledata=rp.read() # read data from source file
                wp.write(srcfiledata) # write source file data to dest file
                print("File Copied Successfully")
    except FileNotFoundError:
        print("Source File Does not Exist")

#Main Program
filecopy()