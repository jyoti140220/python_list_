a=[12,3,4,3,5,7,12,5,8]
b=[]
i=0
while i<len(a):
	if a[i] not in b:
		b.append(a[i])
	i=i+1
print(b)