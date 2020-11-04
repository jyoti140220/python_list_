a=[40,12,30,35,25,27,28,90]
count=0
i=0
while i<len(a):
    if a[i]>20 and a[i]<40:
        count=count+1
    i=i+1
print(count)