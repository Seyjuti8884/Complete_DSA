#tc O(n)
a=[7,3,9,1,2,4]
key=10
for i in range(len(a)):
    if a[i]==key:
        print(i)
        break
else:
    print("-1")

