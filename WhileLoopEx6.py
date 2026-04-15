#Program for accepting a Line of Text and display each and every letter
#WhileLoopEx6.py
word="PYTHON"
print("-"*50)
print("By using while loop--+Ve Indices--Forward Direction")
print("-"*50)
i=0
while(i<len(word)):
    print("\t{}".format(word[i]))
    i=i+1
print("-"*50)
print("By using while loop -Ve Indices--Forward Direction")
print("-"*50)
i=-len(word)
while(i<=-1):
    print("\t{}".format(word[i]))
    i=i+1
print("-"*50)
print("By using while loop +Ve Indices--Backrward Direction")
print("-"*50)
i=len(word)-1
while(i>=0):
    print("\t{}".format(word[i]))
    i=i-1
print("-"*50)
print("By using while loop -Ve Indices--Backrward Direction")
print("-"*50)
i=-1
while(i>=-len(word)):
    print("\t{}".format(word[i]))
    i=i-1
print("-"*50)

