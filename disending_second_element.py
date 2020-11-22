s=[(2,5),(1,2),(4,4),(2,3),(2,1)]
i=0
while i<len(s):
	j=0
	while j<len(s):
		if s[i][1]<s[j][1]:
			s[i],s[j]=s[j],s[i]
		j=j+1
	i=i+1
print(s)