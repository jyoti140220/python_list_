Fibonacci num=int(input("enter num"))
i=1
a=0
b=1
while i<num:
	c=a+b
	a=b
	b=c
	i=i+1
print(a)