s=["A","B"]
n=int(input("enter num"))
i=1
b=[]
while i<=n:
	j=0
	while j<len(s):
		b.append(s[j]+str(i))
		j=j+1
	i=i+1
print(b)