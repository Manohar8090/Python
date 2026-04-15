def kvrcapitalize(s):
	c=""
	for ch in s[1:]:
		if(ord(ch) in range(65,91)):
			c=c+chr(ord(ch)+32)
		else:
				c=c+ch
	if(ord(s[0]) in range(97,123)):
		c=chr(ord(s[0])-32)+c
	else:
		c=s[0]+c
	return c

#Main Program
s=input("Enter any Text:")
x=kvrcapitalize(s)
print("\t",x)