a=[
      [8,5,4],
      [1,6,0],
      [0,2,5]
]
i=0
sum=0
while i<len(a)-1:
	j=0
	while j<len(a[i]):
		if a[i+1][j]!=0:
			sum=sum+a[i][j]	
		j=j+1
	i=i+1
i=2
while i<=2:
	sum2=0
	j=0
	while j<len(a[i]):
		if a[i-1][j]!=0:
			sum2=sum2+a[i][j]
		j=j+1
	i=i+1
print(sum2+sum)