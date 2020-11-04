n=[50, 40, 23, 70, 56, 12, 5, 10, 7]
max=0
second_max=0
i=0
while i<len(n):
    if n[i]>max:
        max=n[i]
    i=i+1
j=0
while j<len(n):
    if n[j]>second_max and n[j]!=max:
        second_max=n[j]
    j=j+1
print(second_max)


