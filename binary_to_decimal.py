binary=[1,0,1,0]
i=len(binary)-1
count=0
cal=1
while i>=0:
    count=count+(binary[i]*cal)
    cal=cal*2
    i=i-1
print(count)