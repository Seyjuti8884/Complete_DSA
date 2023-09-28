n = input()
l = {x: n.count(x) for x in set(n)}
print(str(l))

