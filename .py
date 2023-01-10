a=[['gabriel', 124, 456], ['bruna', 1346, 321], ['joao', 322121, 54]]
c=[]

for i in a:
    print(i)
    c.append(i[1])

print(c.index(124))


print(a[1][2])

for i in range(len(a)):
    print(i)