l1=[12,-7,5,64,-14]
l2=[12,14,-95,3]
for num in l1:
    if num<0:
        l1.remove(num)
    else:
        continue
print(*l1)
for num in l2:
    if num<0:
        l2.remove(num)
    else:
        continue
print(l2)
