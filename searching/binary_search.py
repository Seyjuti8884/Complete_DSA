
#tc o(logn)
#soted array
#fast
a=[1,2,3,4,5,6,7,8]
target=18
low=0
high=len(a)-1
while low<=high:
    mid=(low+high)//2
    if a[mid]==target:
        print(a[mid])
        break
    elif a[mid]<target:
        low=mid+1
    else:
        high=mid-1
else:
    print("-1")