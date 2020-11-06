a=[
   [8,3,4],
   [1,5,9],
   [6,7,2]
]
i=0
sum=0
L_digo=0
R_digo=0
while i<len(a):
	raw=0
	colm=0
	j=0
	while j<len(a[i]):
		raw=raw+a[i][j]
		colm=colm+a[j][i]
		if i==2-j:
			L_digo=L_digo+a[i][j]
		if i==j:
			R_digo=R_digo+a[i][j]
		j=j+1
	i=i+1
	print(i,"raw ka sum:-",raw)
	print(i,"colum ka sum:-",colm)
print("left digonal ka sum",L_digo)
print("right digonal ka sum",R_digo)
print()
if raw==colm==L_digo==R_digo:
    print("it is magic squre")
else:
    print("it is not magic squre")