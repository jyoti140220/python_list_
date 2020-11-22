a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
b=[]
i=0
while i<=2:
	j=i
	c=[]
	while j<len(a):
		c.append(a[j])
		j=j+3
	b.append(c)
	i=i+1
print(b)