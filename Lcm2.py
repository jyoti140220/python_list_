n1=int(input("enter the num"))
n2=int(input("enter the num"))
i=1
while n1>0:
	if i%n1==0 and i%n2==0:
		print(i)
		break
	i=i+1