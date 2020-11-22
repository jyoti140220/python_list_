i=1
z=0
p=0
n=0
e=0
o=0
while i<=10:
	num=int(input("enter the num"))
	if num==0:
		z=z+1
	if num>0:
		p=p+1
	if num<0:
		n=n+1
	if num%2==0 and num>0:
		e=e+1
	if num%2!=0 and num>0:
		o=o+1
	i=i+1
print("zero :",z)
print("positive :",p)
print("negetive :",n)
print("even :",e)
print("odd :",o)