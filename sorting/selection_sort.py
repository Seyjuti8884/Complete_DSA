a=[45,12,34,67,20]
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            c=a[i]
            a[i]=a[j]
            a[j]=c
print(a)