i=1
a=[]
while i<=5:
	num=int(input("enter the num"))
	a.append(num)
	i=i+1
n=int(input("enter the nm"))
if n in a:
     print("present")
else:
     print("upsent")