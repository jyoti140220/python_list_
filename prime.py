n=[5,2,12,6,7,8,11]
a=[]
i=0
while i<=len(n):   
    j=1
    while j<=n[i]:
        if a[i]%a[i]==0 and a[i]%1==0:
            if a[i]%j!=0:
                a.append(n[i])
        j=j+1
    i=i+1
print(a)