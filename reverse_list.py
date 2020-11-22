i=1
a=[]
while i<=5:
	num=int(input("enter the num"))
	a.append(num)
	i=i+1
print(a)
i=1
c=[]
while i<=len(a):
	c.append(a[-i])
	i=i+1
print(c)