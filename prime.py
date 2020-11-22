a=[5,17,8,9,7,6,11]
b=[]
i=0
while i<len(a):
	j=2
	while j<a[i]:
		if a[i]%j==0:
			break
		j=j+1
	else:
		b.append(a[i])
	i=i+1
print(b)