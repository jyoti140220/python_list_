a=[16,-45,5,2,99,-2]
i=0
while i<len(a):
	j=0
	while j<len(a):
		if a[i]<0:
			a[i]=a[i]
		elif a[i]<a[j]:
			a[i],a[j]=a[j],a[i]
		j=j+1
	i=i+1
print(a)