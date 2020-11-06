a=[1,23,11,12,13,15,24]
i=0
while i<len(a):
	j=0
	while j<len(a):
		if a[i]<a[j]:
			a[i],a[j]=a[j],a[i]
		j=j+1
	i=i+1
print(a)