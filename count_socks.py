n=int(input("enter the num :"))
i=1
a=[]
while i<=n:
	num=int(input("enter num :"))
	a.append(num)
	i=i+1
x=a
print(x)
i=0
y=[]
while i<len(x):
	if x[i] not in y:
		y.append(x[i])
	i=i+1
print(y)
i=0
sum=0
while i<len(y):
	j=0
	count=0
	while j<len(x):
		if y[i]==x[j]:
			count=count+1
		j=j+1
	a=count
	s=(a//2)
	sum=sum+s	
	i=i+1
print(sum)