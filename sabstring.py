m="the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
a=m.split()
i=0
s=" "
while i<len(a):
    if a[i]=="over":
        s="on"
    else:
        s=a[i]
    i=i+1
    print(s,end=" ")
