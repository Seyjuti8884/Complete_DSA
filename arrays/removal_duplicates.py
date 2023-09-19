a=[1,1,2,2,3,3,4]
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)
