n=[90,78,56,89,102,91]
i=0
max=0
s_max=0
while i<len(n):
    if n[i]>max:
        max=n[i]
    i=i+1
    if i==len(n):
        j=0
        while j<len(n):
            if n[j]<max and n[j]>s_max:
                s_max=n[j]
            j=j+1
        print(s_max)