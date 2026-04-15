#Program for accepting a Line of Text and display each and every letter
#ForLoopEx4.py
s="PYTHON"
print("-------------------------------------------------")
print("By using for loop in forward direction without indices")
for ch in s:
    print("\t{}".format(ch))
print("-------------------------------------------------")
print("By using for loop in backward direction without indices")
for ch in s[::-1]:
    print("\t{}".format(ch))
print("-------------------------------------------------")
print("By using for loop in forward direction with +ve indices")
for i in range(0,len(s)):
    print("\t{}".format(s[i]))
print("-------------------------------------------------")
print("By using for loop in forward direction with -ve indices")
for i in range(-len(s),0):
    print("\t{}".format(s[i]))
print("-------------------------------------------------")
print("By using for loop in backrward direction with +ve indices")
for i in range(len(s)-1,-1,-1):
    print("\t{}".format(s[i]))
print("-------------------------------------------------")
print("By using for loop in backrward direction with -ve indices")
for i in range(-1,-(len(s)+1),-1):
    print("\t{}".format(s[i]))
print("-------------------------------------------------")
