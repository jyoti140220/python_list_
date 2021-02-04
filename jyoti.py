s=["ab","xyz","ab","1221"]
i=0
c=0
k=len(s[i])
while i<len(s):
    if k>=2 and s[i][0]==s[i][-1]:
        c=c+1
    i=i+1
print(c)