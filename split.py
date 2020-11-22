s="this is my book"
sp=[]
tem=" "
i=0
while i<len(s):
	if s[i]==" ":
		sp.append(tem)
		tem=" "
	else:
		tem+=s[i]
	i=i+1
if tem:
	sp.append(tem)
print(sp)