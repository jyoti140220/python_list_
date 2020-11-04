a=[23,56,5,44,12,33,67,89,10]
b=[]
i=0
while i<len(a):
    if a[i]%2!=0:
        b.append(a[i])
    i=i+1
print(b)
