n=list(input("enter list : "))
a=[]
i=0
while i<len(n):
    t=n[-i-1]
    a.append(t)
    i=i+1
print(a==n)