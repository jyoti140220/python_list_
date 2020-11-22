s=["A","B"]
i=0
n=int(input("enter num"))
b=[]
while i<len(s):
	j=1
	while j<=n:
		b.append(s[i]+str(j))
		j=j+1
	i=i+1
print(b)