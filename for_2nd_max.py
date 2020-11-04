a=[34,46,87,68,90,34,67,89,78,]
max=0
sec_max=0
for x in a:
    if x>max:
        max=x
print("1st maximum",max)
for y in a:
    if y>sec_max and y!=max:
        sec_max=y
print("2nd maximum",sec_max)