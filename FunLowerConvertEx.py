#program for accepting a Line of Text and Convert into Lower and upper
# without using user lower() and upper()
#FunLowerConvertEx.py
def getline():
    return input("Enter Line of Text:")

def kvrlower(line):
    lc=""
    for ch in line:
        if(ord(ch) in range(65,91)):
            lc=lc+chr(ord(ch)+32)
        else:
            lc=lc+ch
    return lc
def kvrupper(line):
    uc=""
    for ch in line:
        if(ord(ch) in range(97,123)):
            uc=uc+chr(ord(ch)-32)
        else:
            uc=uc+ch
    return uc
#Main Program
line=getline()
lu=kvrlower(line)
ul=kvrupper(line)
print("-----------------------------")
print("Given Line=",line)
print("Lower Case Line=",lu)
print("Upper Case Line=",ul)
print("-----------------------------")

